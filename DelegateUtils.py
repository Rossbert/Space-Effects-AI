import numpy as np
import tensorflow as tf
import numpy.typing as npt
from typing import List, Tuple
from enum import IntEnum

class OperationMode(IntEnum):
    """ Operation modes for the custom delegates """
    none = 0
    weights = 1
    convolution = 2

def get_operation_mode(operation_mode : OperationMode) -> str:
    """ Gets the operation mode in string form """
    match operation_mode:
        case OperationMode.none:
            return "none"
        case OperationMode.weights:
            return "weights"
        case OperationMode.convolution:
            return "convolution"
        case _ :
            return "error"

def get_bits_size(operation_mode: OperationMode) -> int:
    """ Gets the bit number of the operation """
    match operation_mode:
        case OperationMode.convolution:
            return 32
        case OperationMode.weights:
            return 8
        case _ :
            return -1
        

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

