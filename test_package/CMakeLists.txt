PROJECT(PackageTest)
cmake_minimum_required(VERSION 2.8.12)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

ADD_EXECUTABLE(simplejsontest simplejsontest.cpp)
TARGET_LINK_LIBRARIES(simplejsontest ${CONAN_LIBS})
