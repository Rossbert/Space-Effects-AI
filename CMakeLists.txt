cmake_minimum_required(VERSION 3.10)
project(custom_delegates)

set(TENSORFLOW_SRC "C:/Users/rosal/Documents/Files/Master\ Project/tensorflow_src")
set(TENSORFLOW_BUILD "C:/Users/rosal/Documents/Files/Master\ Project/tflite-v2.15.0")

# Set configurations
set(CMAKE_CONFIGURATION_TYPES "Release;Test" CACHE STRING "Configs" FORCE)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Define custom linker flags for the "Test" configuration
set(CMAKE_SHARED_LINKER_FLAGS_TEST "/INCREMENTAL:NO")

# Set platform to x64
set(CMAKE_GENERATOR_PLATFORM x64)

# Define the source files
set(SOURCE_FILES
    src/ConvOps.h
    src/ConvOps.cpp
    src/ConvTemplates.h
    src/DelegateCore.h
    src/DelegateCore.cpp
    src/EntryPoint.cpp
    src/FullyConnectedOps.h
    src/FullyConnectedOps.cpp
    src/FullyConnectedTemplates.h
    src/Logger.h
    src/Logger.cpp
    src/Options.h
    src/Options.cpp
    ${TENSORFLOW_SRC}/tensorflow/lite/delegates/utils/simple_delegate.cc
)

# Define the include directories
set(INCLUDE_DIRS
    ${TENSORFLOW_SRC}
    ${TENSORFLOW_BUILD}/gemmlowp
)

# Define the library directories
set(LIB_DIRS
    ${TENSORFLOW_BUILD}/tensorflow-lite/Release
)

# Add the dynamic library target
add_library(custom_delegates SHARED ${SOURCE_FILES})

# Set the include directories
target_include_directories(custom_delegates PRIVATE     
    ${INCLUDE_DIRS}
)

# Set the library directories
target_link_directories(custom_delegates PRIVATE ${LIB_DIRS})

# Link against the TensorFlow Lite library
target_link_libraries(custom_delegates PRIVATE tensorflow-lite)

# Set compiler options
target_compile_options(custom_delegates PRIVATE
    /W3 /wd4244 /wd4267 /wd4996 /permissive-
)

# Set linker options
target_link_options(custom_delegates PRIVATE
    /IGNORE:4099
)

# Set preprocessor definitions based on configuration
target_compile_definitions(custom_delegates PRIVATE
    $<$<CONFIG:Release>:TFL_COMPILE_LIBRARY;NDEBUG;RELEASE_CONFIG;_CONSOLE> 
    $<$<CONFIG:Test>:TFL_COMPILE_LIBRARY;NDEBUG;TEST_CONFIG;_CONSOLE;LOGGER> 
    # TFL_COMPILE_LIBRARY NDEBUG _CONSOLE
)

# Set the output directory
set_target_properties(custom_delegates PROPERTIES
    ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib
    LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin
    RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin
)

# Copy the built DLL to the specified directory
add_custom_command(TARGET custom_delegates POST_BUILD
    COMMAND ${CMAKE_COMMAND} -E copy
    $<TARGET_FILE:custom_delegates>
    "${CMAKE_CURRENT_SOURCE_DIR}/dependencies"
)
