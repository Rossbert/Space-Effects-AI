# Space Effect AI project v1.0.0
This repository will give you the basic steps and the source code to compile a Tensor Flow Lite custom delegate to simulate random bit flipping (SET or SEU) in the weights and during the convolution multiplication of a convolutional neural network.
## Prerequisites
###
    Python v3.10.4
    Tensorflow python package v2.11.0
    Tensorflow Lite v2.15.0 built library from source (Refer to the Readme Prerequisited.md for details)
    VisualStudio 17 2022 (Windows only, recommended)
## Install Python
Python v3.10.4 is required for the project to work, feel free to choose the installation method you prefer.
## Install Tensorflow 
Install the version 2.11.0 using pip
```bash
pip install tensorflow==2.11.0
```
## Build Tensorflow Lite from source
Refer to the `Readme Prerequisites.md` file to build Tensorflow Lite from source.
## Use the python workbenchs to test the Space Effects AI delegates
There are 3 predefined workbenchs to test the generated delegates.
* `workbench_set_simple.py`
* `workbench_set_loop.py`
* `workbench_efficientnet.py`

Use the `workbench_set_simple.py` script to test a single simulation run of the custom delegate and generate accuracy data using the MNIST Fashion dataset.
The following variables in the file describe the inputs for the script. 
```python
N_SIMULATIONS = 10
N_FLIPS_LIMIT = 4
LAYERS = ("conv2d/", "conv2d_1/", "conv2d_2/", "last/")
TFLITE_PATH = "./model/tflite_ep5_2023-07-02_16-50-58.tflite"
DELEGATE_PATH = "./dependencies/custom_delegates.dll"
OUTPUTS_DIR = "./outputs/"
```
* `LAYERS` indicates the name of the layers that the current Tensorflow Lite model interpreter has.
* `TFLITE_PATH` indicates the location of the model interpreter.
* `DELEGATE_PATH` indicates the location of the generated delegate in the `Space Effects AI` project.
* `OUTPUTS` indicates the location of the output data.

Use the `workbench_set_loop.py` script to test a loop simulation run of the custom delegate and generate accuracy data using the MNIST Fashion dataset.
In addition of the previously described variables, the file requires more inputs. 

```python
OPERATION_MODES = (OperationMode.convolution, OperationMode.weights)
N_SIMULATIONS = 25
NUM_BITS_TO_FLIP = (1, 2, 4)
```
* `OPERATION_MODES` describes the possible operations that the custom delegate will affect: either a direct effect on the weights of the net or the accumulator during the convolution operation.
* `N_SIMULATIONS` indicates the number of repetitions the whole simulation will be executed.
* `N_FLIPS_LIMIT` indicates the number of consecutive flips that will be performed during the execution of the loops.

Use the `workbench_efficientnet.py` script to test a single simulation run of the custom delegate and generate accuracy data using the validation data of the ImageNet dataset (ILSVRC-2012-CLS). The model used for this simulation is EfficientNet_B7, obtained from Kaggle.
The same variables described before are required with the following additions: 
```python
TFLITE_PATH = "C:\\Users\\rosal\\Documents\\Files\\Master Project\\New Model\\EfficientNet\\2.tflite"
IMAGE_DIR = "C:\\Users\\rosal\\Documents\\Files\\Master Project\\New Model\\EfficientNet\\ILSVRC2012\\ILSVRC2012_devkit_t12\\data"
TRUE_LABELS = IMAGE_DIR + "\\ILSVRC2012_validation_ground_truth.txt"
MATCHING_LABELS = "C:\\Users\\rosal\\Documents\\Files\\Master Project\\New Model\\EfficientNet\\ILSVRC2012\\Labels_Final.csv"
```
* `TFLITE_PATH` indicates the location of the model interpreter of `EfficientNet_B7`.
* `IMAGE_DIR` indicates the location of the dataset images.
* `TRUE_LABELS` indicates the file name containing the true labels of the validation dataset.
* `MATCHING_LABELS` indicates the matching labels to correct the discrepancy between the numbering of the labels during training and the labels in the validation dataset.

`Take care into consideration that the layers names are described in the model metadata, use the names specified in the following section to use the delegetes correctly.`
<!-- Used models for testing
model: tflite_ep5_2023-07-02_16-50-58.tflite
pretrained on: MNIST Fashion
Accuracy : 91.4%
Loss: 0.38962257
Evaluation time = 1.91 seconds

model: EfficientNet_B7
pretrained on: ImageNet (ILSVRC-2012-CLS)
Accuracy : 76.31%
Loss: 1.145592
Evaluation time = 3178.854 seconds = 52.98 min
-->

## Model names for tensors 
For the `tflite_ep5_2023-07-02_16-50-58` model the layer names are described as follows:
* "conv2d/"
* "conv2d_1/"
* "conv2d_2/"
* "last/"

For the `EfficientNet_B7` model the layer names are described fully in the comments of this file. A snippet is shown as follows:
* "stem/tpu_batch_normalization/"			
* "blocks_0/tpu_batch_normalization/"		
* "blocks_0/tpu_batch_normalization_1/"	
* "blocks_1/tpu_batch_normalization/"		
* "blocks_1/tpu_batch_normalization_1/"	
* "blocks_1/tpu_batch_normalization_2/"	
* "blocks_2/tpu_batch_normalization/"
* ...
<!-- model: EfficientNet_B7
Layer names:
stem/tpu_batch_normalization/			
blocks_0/tpu_batch_normalization/		
blocks_0/tpu_batch_normalization_1/	
blocks_1/tpu_batch_normalization/		
blocks_1/tpu_batch_normalization_1/	
blocks_1/tpu_batch_normalization_2/	
blocks_2/tpu_batch_normalization/		
blocks_2/tpu_batch_normalization_1/	
blocks_2/tpu_batch_normalization_2/	
blocks_3/tpu_batch_normalization/		
blocks_3/tpu_batch_normalization_1/	
blocks_3/tpu_batch_normalization_2/	
blocks_4/tpu_batch_normalization/		
blocks_4/tpu_batch_normalization_1/	
blocks_4/tpu_batch_normalization_2/	
blocks_5/tpu_batch_normalization/		
blocks_5/tpu_batch_normalization_1/	
blocks_5/tpu_batch_normalization_2/	
blocks_6/tpu_batch_normalization/		
blocks_6/tpu_batch_normalization_1/	
blocks_6/tpu_batch_normalization_2/	
blocks_7/tpu_batch_normalization/		
blocks_7/tpu_batch_normalization_1/	
blocks_7/tpu_batch_normalization_2/	
blocks_8/tpu_batch_normalization/		
blocks_8/tpu_batch_normalization_1/	
blocks_8/tpu_batch_normalization_2/	
blocks_9/tpu_batch_normalization/		
blocks_9/tpu_batch_normalization_1/	
blocks_9/tpu_batch_normalization_2/	
blocks_10/tpu_batch_normalization/	
blocks_10/tpu_batch_normalization_1/	
blocks_10/tpu_batch_normalization_2/	
blocks_11/tpu_batch_normalization/	
blocks_11/tpu_batch_normalization_1/	
blocks_11/tpu_batch_normalization_2/	
blocks_12/tpu_batch_normalization/	
blocks_12/tpu_batch_normalization_1/	
blocks_12/tpu_batch_normalization_2/	
blocks_13/tpu_batch_normalization/	
blocks_13/tpu_batch_normalization_1/	
blocks_13/tpu_batch_normalization_2/	
blocks_14/tpu_batch_normalization/	
blocks_14/tpu_batch_normalization_1/	
blocks_14/tpu_batch_normalization_2/	
blocks_15/tpu_batch_normalization/	
blocks_15/tpu_batch_normalization_1/	
blocks_15/tpu_batch_normalization_2/	
blocks_16/tpu_batch_normalization/	
blocks_16/tpu_batch_normalization_1/	
blocks_16/tpu_batch_normalization_2/	
blocks_17/tpu_batch_normalization/	
blocks_17/tpu_batch_normalization_1/	
blocks_17/tpu_batch_normalization_2/	
blocks_18/tpu_batch_normalization/	
blocks_18/tpu_batch_normalization_1/	
blocks_18/tpu_batch_normalization_2/	
blocks_19/tpu_batch_normalization/	
blocks_19/tpu_batch_normalization_1/	
blocks_19/tpu_batch_normalization_2/	
blocks_20/tpu_batch_normalization/	
blocks_20/tpu_batch_normalization_1/	
blocks_20/tpu_batch_normalization_2/	
blocks_21/tpu_batch_normalization/	
blocks_21/tpu_batch_normalization_1/	
blocks_21/tpu_batch_normalization_2/	
blocks_22/tpu_batch_normalization/	
blocks_22/tpu_batch_normalization_1/	
blocks_22/tpu_batch_normalization_2/	
blocks_23/tpu_batch_normalization/	
blocks_23/tpu_batch_normalization_1/	
blocks_26/tpu_batch_normalization/	
blocks_26/tpu_batch_normalization_1/	
blocks_26/tpu_batch_normalization_2/	
blocks_27/tpu_batch_normalization/	
blocks_27/tpu_batch_normalization_1/	
blocks_27/tpu_batch_normalization_2/	
blocks_28/tpu_batch_normalization/	
blocks_28/tpu_batch_normalization_1/	
blocks_28/tpu_batch_normalization_2/	
blocks_29/tpu_batch_normalization_1/	
blocks_29/tpu_batch_normalization_2/	
head/tpu_batch_normalization/			
head/dense/MatMul
-->