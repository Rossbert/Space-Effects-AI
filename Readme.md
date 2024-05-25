# Create your own Tensor Flow Lite delegate to affect weights and convolution

This repository will give you the basic source code to compile a Tensor Flow Lite Delegate to simulate random bit flipping in the weights and during the convolution multiplication.

## Tensor Flow Delegate compilation

The C++ code requires that you have downloaded and compiled Tensor Flow Lite from source in a static library.

- Modify the CMakeLists.txt as required to specify the Tensor Flow Lite source and compiled library paths.
- Build the project and the output library will be copied into the ./dependencies folder 

## Tensor Flow Custom Delegate testing

Use the delegates_set.py script to test the delegate and generate accuracy data using the MNIST Fashion dataset.

# Used versions

Real commit ID for TFLite
ea0637ac525b4b1e1794373014f1159a7e13ebcb

Author: Bing Hu <binghu@google.com>
Date:   Wed Sep 20 14:05:44 2023 -0700

    Mesh creation API should also support taking a list of DeviceSpec as input

    PiperOrigin-RevId: 567074638

Standarize everything to:
v2.14.0 (closer) 4dacf3f368eb7965e9b5c3bbdd5193986081c3b2
Merge pull request #61943 from georgiyekkert/r2.14

# Add this inside CMakeLists.txt
if(${CMAKE_SYSTEM_NAME} MATCHES "Windows")
  # See https://github.com/tensorflow/tensorflow/blob/\
  # 2b96f3662bd776e277f86997659e61046b56c315/tensorflow/lite/tools/make/\
  # Makefile#L157
  set(_TFLITE_ENABLE_MMAP OFF)
  add_compile_definitions(TFLITE_MMAP_DISABLED) # This line!
endif()


# Anotations for new model to be used
model used: EfficientNet_B7
pretrained on: ImageNet (ILSVRC-2012-CLS)

For the complete dataset of 50000
Model accuracy : 76.31%
Model loss: 1.145592
Evaluation time 3178.854 seconds = 52.98 min

# Model names for tensors 
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