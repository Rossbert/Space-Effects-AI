# Space Effect AI project v1.0.0 prerequisites
The present project aims to study the effects of SETs and SEUs in CNN frameworks. This guide will help you to build the project from scratch. 

## Prerequisites
The following programs are required, the indicated versions were used to test the project. It is not guaranteed that other versions will work:
###
    CMake v3.16 (Tested with v3.27.5)
    VisualStudio 17 2022 (Windows only, recommended)

## Build Tensorflow Lite from source for Linux
In order to build Tensorflow Lite from source you must clone the Tensorflow repository into your local machine.
* Create a project folder (e.g. `PROJECT_DIR_NAME`) and navigate to it. 

* Clone the v2.15.0 tag from the Tensorflow repository using the command:
```bash
git clone --branch v2.15.0 --depth 1 https://github.com/tensorflow/tensorflow.git TFLITE_SRC_DIR
```
Replace `TFLITE_SRC_DIR` with a directory name of your choosing.

* Create a folder to build Tensorflow Lite and navigate to it.
```bash
mkdir tflite-v2.15.0
cd tflite-v2.15.0
```
You can use a different build file name instead of `tflite-v2.15.0`

* Generate the build files using the path to the cloned repository:
```bash
cmake -DCMAKE_BUILD_TYPE=Release ./TFLITE_SRC_DIR/tensorflow/lite/c
```

* Build the project:
```bash
cmake --build .
```

`You will find the generated shared library in the following path:`.
```
PROJECT_DIR_PATH/tflite-v2.15.0/libtensorflow-lite.so
```

## Build Tensorflow Lite from source for Windows
`In order to build Tensorflow Lite for Windows it is recommended to use VisualStudio 17 2022.`

You need to follow the same steps of before up until before building Tensorflow Lite.
* Follow the previous steps like the Linux version up until before executing the `cmake` commands

`Building the default project generates an error during compilation. In order to avoid this issue follow these steps before building the project with CMake`
* Navigate to the following folder:
```bash
cd ./TFLITE_SRC_DIR/tensorflow/lite/
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
    Where is the source code: PROJECT_DIR_PATH/TFLITE_SRC_DIR/tensorflow/lite/c
    Where to build the binaries: PROJECT_DIR_PATH/tflite-v2.15.0
* Click on `Configure`. 

The application will ask about the generator for the project.
* Select `VisualStudio 17 2022` and platform `x64`. Click on `Finish`
* Click on `Generate`.
* Click on `Open Project`.

The VisualStudio project solution will be opened.
* Select `Release` as Configuration and `x64` as platform.

* Click on `Build` and then `Build Solution`.

`You will find the generated dynamic library in the following path:`.
```
PROJECT_DIR_PATH/tflite-v2.15.0/Release/tensorflowlite_c.dll
```

## Build the Space Effect AI project library
This section of the tutorial will focus on the compilation of the source code to generate the libraries for the custom delegates of the Space Effects AI project.

* Navigate to your project folder (`PROJECT_DIR_NAME`). 
```bash
cd PROJECT_DIR_PATH
```
* Clone the Space Effects AI project repository using the command:
```bash
git clone https://github.com/Rossbert/Space-Effects-AI.git Space_Effects_AI
```
You can replace `Space_Effects_AI` with a name of your choosing. 
* Navigate to the `Space_Effects_AI` folder.
```bash
cd Space_Effects_AI
```
* Modify the paths inside the `CMakeLists.txt` file to generate the project in lines 4 and 5:
The resulting file should look like this:
```CMake
cmake_minimum_required(VERSION 3.10)
project(custom_delegates)

set(TENSORFLOW_SRC "PROJECT_DIR_PATH/TFLITE_SRC_DIR")
set(TENSORFLOW_BUILD "PROJECT_DIR_PATH/tflite-v2.15.0")

```
* Create the build folder.
```bash
mkdir build
```

## Building for Linux
* Navigate to the build folder.
```bash
cd build
```
* Generate the build files using the path to the cloned repository:
```bash
cmake -DCMAKE_BUILD_TYPE=Release ..
```
* Build the project:
```bash
cmake --build .
```
## Building for Windows
* Open the `CMake` application. 

* Specify the following fields:
#
    Where is the source code: PROJECT_DIR_PATH/Space_Effects_AI
    Where to build the binaries: PROJECT_DIR_PATH/Space_Effects_AI/build
* Click on `Configure`. 

The application will ask about the generator for the project.
* Select `VisualStudio 17 2022` and platform `x64`. Click on `Finish`
* Click on `Generate`.
* Click on `Open Project`.

The VisualStudio project solution will be opened.
* Select `Release` as Configuration and `x64` as platform.

* Click on `Build` and then `Build Solution`.

`You will find the generated dynamic library in the following path:`.
```
PROJECT_DIR_PATH/Space_Effects_AI/dependencies/custom_delegates.dll
```


``` To use the Space Effect AI project please refer to the Readme.md file ```