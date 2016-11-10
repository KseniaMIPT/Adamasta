cmake_minimum_required(VERSION 3.3)
project(circular_buffer)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")

set(SOURCE_FILES main.cpp)
add_executable(circular_buffer ${SOURCE_FILES})