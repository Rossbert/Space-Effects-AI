# Space Effect AI project v1.0.0
The present project aims to study the effects of SETs and SEUs in CNN frameworks. This guide will help you to build the project from scratch. 

The following programs are required, the indicated versions were used to test the project. It is not guaranteed that other versions will work:
###
    Python v3.10.4
    Tensorflow python package v2.11.0
    Tensorflow repository v2.15.0 (to build TFLite for C++)
    VisualStudio 17 2022 (Windows only, recommended)

## Installation steps

### Install Python

Python v3.10.4 is required for the project to work, feel free to choose the installation method.

### Install Tensorflow 
Install the version 2.11.0 using pip
```bash
pip install tensorflow==2.11.0
```
### Build Tensorflow Lite from source for Linux
In order to build Tensorflow Lite from source you must clone the Tensorflow repository into your local machine.
* Create a project folder (e.g. `PROJECT_DIR_NAME`) and navigate to it. 

* Clone the v2.15.0 tag from the Tensorflow respository using the command:
```bash
git clone --branch v2.15.0 --depth 1 https://github.com/tensorflow/tensorflow.git CLONE_DIR_NAME
```
Replace `CLONE_DIR_NAME` with a directory name of your choosing.

* Create a folder to build Tensorflow Lite and navigate to it.
```bash
mkdir tflite-v2.15.0
cd tflite-v2.15.0
```
You can use a different build file name instead of `tflite-v2.15.0`

* Generate the build files using the path to the cloned repository:
```bash
cmake -DCMAKE_BUILD_TYPE=Release ./CLONE_DIR_NAME/tensorflow/lite/c
```

* Build the project:
```bash
cmake --build .
```

`You will find the generated dynamic library in the following path:`.
```
PROJECT_DIR_PATH/tflite-v2.15.0/libtensorflow-lite.so
```

### Build Tensorflow Lite from source for Windows
`In order to build Tensorflow Lite for Windows it is recommended to use VisualStudio 17 2022.`

You need to follow the same steps of before up until before building Tensorflow Lite.
* Follow the previous steps like the Linux version up until before executing the `cmake` commands

`Building the default project generates an error during compilation. In order to avoid this issue follow these steps before building the project with CMake`
* Navigate to the following folder:
```bash
cd ./CLONE_DIR_NAME/tensorflow/lite/
```
* Modify the CMakeLists.txt file by adding the following text in line 100:
###
    add_compile_definitions(TFLITE_MMAP_DISABLED)

Here there is a snippet of how the result file should look like:
```CMake
if(${CMAKE_SYSTEM_NAME} MATCHES "Windows")
  # See https://github.com/tensorflow/tensorflow/blob/\
  # 2b96f3662bd776e277f86997659e61046b56c315/tensorflow/lite/tools/make/\
  # Makefile#L157
  set(_TFLITE_ENABLE_MMAP OFF)
  add_compile_definitions(TFLITE_MMAP_DISABLED) # Add this line!
endif()
```
* Navigate to the build folder.
```bash
cd tflite-v2.15.0
```
* Build the project using the commands like in the Linux installation steps or, you can use the CMake app for Windows:

`In case you use the CMake application for Windows follow the next steps:`
* Open the `CMake` application. 

* Specify the following fields:
#
    Where is the source code: PROJECT_DIR_PATH/CLONE_DIR_NAME/tensorflow/lite/c
    Where to build the binaries: PROJECT_DIR_PATH/tflite-v2.15.0
* Click on `Configure`. 

The application will ask about the generator for the project.
* Select `VisualStudio 17 2022` and platform `x64`.
* Click on `Generate`.
* Click on `Open Project`.

The VisualStudio project solution will be opened.
* Select `Release` as Configuration and `x64` as platform.

* Click on `Build` and then `Build Solution`.

`You will find the generated dynamic library in the following path:`.
```
PROJECT_DIR_PATH/tflite-v2.15.0/Release/tensorflowlite_c.dll
```


