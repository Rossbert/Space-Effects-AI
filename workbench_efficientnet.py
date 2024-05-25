import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import time
import random
import os
import csv
import datetime
import numpy.typing as npt
from typing import List, Tuple
import DelegateUtils

def evaluate_ninput_model(interpreter: tf.lite.Interpreter, dataset_inputs: dict, dataset_labels: npt.NDArray) -> Tuple[float, float, List[npt.NDArray]]:
    """ Evaluate TFLite Model:
    - Receives the interpreter and returns addition of inputs
    """
    # print(interpreter.get_input_details())
    # print(interpreter.get_tensor_details())
    dataset_size = len(dataset_inputs)
    predicted_categories = []
    outputs = []
    # For the number of inputs
    for k in range(dataset_size):
        # For the length of the dataset
        interpreter.set_tensor(
            tensor_index = interpreter.get_input_details()[0]["index"], 
            value = dataset_inputs[k, :][np.newaxis, :])
        
        idx_output = interpreter.get_output_details()[0]["index"]

        # Run inference.
        interpreter.invoke()

        # Post-processing
        # output = interpreter.tensor(idx_output)
        output = interpreter.get_tensor(idx_output)

        outputs.append(output[0])
        category = np.argmax(output[0])
        predicted_categories.append(category)

        # print(f"{output[0]} => predicted label: {digit} - real label: {dataset_labels[k]}")

    # Compare prediction results with ground truth labels to calculate accuracy.
    predicted_categories = np.array(predicted_categories)
    outputs = np.array(outputs)
    scce = tf.keras.losses.SparseCategoricalCrossentropy()(dataset_labels, outputs)

    loss = scce.numpy()
    accuracy = (predicted_categories == dataset_labels).mean()
    return loss, accuracy, outputs

# Función para cargar y preprocesar imágenes
def load_and_preprocess_image(image_path):
    """ Loads the image to be processed """
    # Leer la imagen
    image = tf.io.read_file(image_path)
    # Decodificar la imagen JPEG
    image = tf.image.decode_jpeg(image, channels = 3)
    # Redimensionar la imagen a 300x300 píxeles con crop o pad
    image = tf.image.resize_with_crop_or_pad(image, target_height = 300, target_width = 300)
    # Normalizar la imagen a valores en el rango [0, 1]
    # image = tf.image.convert_image_dtype(image, tf.float32)
    return image

# Función para realizar predicciones con el modelo TensorFlow Lite
def predict_with_tflite(interpreter: tf.lite.Interpreter, dataset, dataset_labels: npt.NDArray):
    input_index = input_details[0]['index']
    output_index = output_details[0]['index']
    
    predicted_categories = []
    outputs = []
    for batch in dataset:
        batch = batch.numpy()  # Convertir el batch a numpy array
        interpreter.set_tensor(input_index, batch)
        interpreter.invoke()
        output = interpreter.get_tensor(output_index)

        outputs.append(output[0]*output_scale)
        category = np.argmax(output[0])
        # print(category)
        predicted_categories.append(category)

    # Compare prediction results with ground truth labels to calculate accuracy.
    predicted_categories = np.array(predicted_categories)
    outputs = np.array(outputs)
    scce = tf.keras.losses.SparseCategoricalCrossentropy()(dataset_labels, outputs)

    loss = scce.numpy()
    accuracy = (predicted_categories == dataset_labels).mean()
    print(f"Model accuracy : {accuracy:.2%}")
    print(f"Model loss: {loss:.6f}")

LAYERS = ("blocks_26/tpu_batch_normalization_2/", )
OPERATION_MODES = (DelegateUtils.OperationMode.convolution, )
# Load paths
TFLITE_PATH = "C:\\Users\\rosal\\Documents\\Files\\Master Project\\New Model\\EfficientNet\\2.tflite"
DELEGATE_PATH = "./dependencies/custom_delegates.dll"
OUTPUTS_DIR = "./outputs/"
# Dataset directories
IMAGE_DIR = "C:\\Users\\rosal\\Documents\\Files\\Master Project\\New Model\\EfficientNet\\ILSVRC2012\\ILSVRC2012_devkit_t12\\data"
TRUE_LABELS = IMAGE_DIR + "\\ILSVRC2012_validation_ground_truth.txt"
MATCHING_LABELS = "C:\\Users\\rosal\\Documents\\Files\\Master Project\\New Model\\EfficientNet\\ILSVRC2012\\Labels_Final.csv"

if not os.path.exists(OUTPUTS_DIR):
    os.mkdir(OUTPUTS_DIR)

# Interpreter creation
interpreter = tf.lite.Interpreter(model_path = TFLITE_PATH)
interpreter.allocate_tensors()
# print(interpreter.get_input_details())
# print(interpreter.get_tensor_details())
# print(interpreter.get_output_details())

# Image dataset creation
image_paths = [os.path.join(IMAGE_DIR, fname) for fname in os.listdir(IMAGE_DIR) if fname.endswith('.JPEG')]
dataset_size = len(image_paths)
sample_size = 1000
# Set the seed for reproducibility
random.seed(10)
# Generate random numbers from 0 to 49999 without repetition
sample_indexes = random.sample(range(dataset_size), sample_size)
# Get sample paths
sample_paths = [image_paths[i] for i in sample_indexes]

# Crear un dataset de TensorFlow a partir de las rutas de las imágenes
dataset = tf.data.Dataset.from_tensor_slices(sample_paths)
# Aplicar la función de carga y preprocesamiento a cada imagen del dataset
dataset = dataset.map(load_and_preprocess_image)
# Si necesitas convertir el dataset a un formato compatible con TensorFlow Lite (por ejemplo, un batch de imágenes)
batch_size = 1
dataset = dataset.batch(batch_size)
# Displaying the images in the dataset
# for image in dataset.take(5):
#     plt.imshow(image.numpy())
#     plt.axis('off')
#     plt.show()

# Labels creation
special_sort_array = np.loadtxt(TRUE_LABELS, dtype = int)
# Create a DataFrame from the special_sort_array
special_sort_df = pd.DataFrame(special_sort_array, columns = ['ILSVRC2012_ID'])
# Matching labels
df = pd.read_csv(MATCHING_LABELS, delimiter = ';')
# Merge the original DataFrame with the special_sort_df on 'input_value'
merged_df = special_sort_df.merge(df, on = 'ILSVRC2012_ID', how = 'left')
# Extract the 'output_value' column and convert it to a numpy array
full_set_labels = merged_df['Matched index'].to_numpy()
# merged_df.to_csv("./out.csv", sep = ';', index = False)
dataset_labels = np.array([full_set_labels[i] for i in sample_indexes])


# Guardar un lote de imágenes para verificar
for batch in dataset.take(1):
    print(batch.shape)  # Debería ser (batch_size, 300, 300, 3)

# Obtener detalles de entrada y salida
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

output_scale = output_details[0]['quantization_parameters']['scales'][0]
print(output_scale)

# Realizar predicciones con el modelo TensorFlow Lite
evaluation_time = time.time()
predict_with_tflite(interpreter, dataset, dataset_labels)
print(f"Evaluation time {time.time() - evaluation_time:.3f} seconds")

# Evaluate the custom delegate model

bit_position = 31
number_flips = 100
layer_name = LAYERS[0]
operation_mode = OPERATION_MODES[0]
delegate = tf.lite.experimental.load_delegate(
    library = DELEGATE_PATH,
    options = {"layer_name": layer_name, 
                "operation_mode" : int(operation_mode),
                "bit_position": bit_position,
                "number_flips": number_flips,
                "dataset_size": full_set_labels.shape[0]
                })

# Interpreter creation
new_interpreter = tf.lite.Interpreter(model_path = TFLITE_PATH, experimental_delegates = [delegate])
# Allocation of memory
new_interpreter.allocate_tensors()

# Realizar predicciones con el modelo TensorFlow Lite
evaluation_time = time.time()
predict_with_tflite(new_interpreter, dataset, dataset_labels)
print(f"Evaluation time {time.time() - evaluation_time:.3f} seconds")