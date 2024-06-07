# Space Effect AI project v1.0.0
The present project aims to study the effects of SETs and SEUs in CNN frameworks. This guide will help you to build the project from scratch. 

The following programs are required, the indicated versions were used to test the project. It is not guaranteed that other versions will work:
###
    Python v3.10.4
    Tensorflow python package v2.11.0
    Tensorflow repository v2.15.0 (to build TFLite for C++)

## Installation steps

### Install Python

Python v3.10.4 is required for the project to work, feel free to choose the installation method.

### Install Tensorflow 
Install the version 2.11.0 using pip
```
pip install tensorflow==2.11.0
```
### Build TensorflowLite from source for Linux
In order to build TensorflowLite from source you must clone the Tensorflow repository into your local machine.
* Clone the v2.15.0 tag from the Tensorflow respository using the command:
```git
git clone --branch v2.15.0 --depth 1 https://github.com/tensorflow/tensorflow.git <clone_dir_name>
```
Replace `<clone_dir_name>` with the directory name of the cloned repository.

* Navigate to the folder:
###
    <clone-dir_path>\tensorflow\lite\c

* Use CMake to build the project using the CMake file located there:
###
    CMakeLists.txt


### Build TensorflowLite from source for Windows

`Building the default project generates an error during compilation. In order to avoid this issue follow these steps: <strong>BEFORE</strong>   building the project with CMake`
* Navigate to the folder
###
    <clone-dir_path>\tensorflow\lite\
* Modify the CMakeLists.txt file by adding the following text in line 100:
###
    add_compile_definitions(TFLITE_MMAP_DISABLED)

The file should look like this:
```CMake
if(${CMAKE_SYSTEM_NAME} MATCHES "Windows")
  # See https://github.com/tensorflow/tensorflow/blob/\
  # 2b96f3662bd776e277f86997659e61046b56c315/tensorflow/lite/tools/make/\
  # Makefile#L157
  set(_TFLITE_ENABLE_MMAP OFF)
  add_compile_definitions(TFLITE_MMAP_DISABLED) # Add this line!
endif()
```
* Run CMake