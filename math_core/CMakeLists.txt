cmake_minimum_required(VERSION 3.15)
project(MathCore VERSION 1.0.0 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_POSITION_INDEPENDENT_CODE ON)

add_library(math_core_lib STATIC
    src/EquationParser.cpp
    src/Logging.cpp
    src/MathFuncs.cpp
    src/Slice.cpp
    src/Token.cpp
    src/Unittest.cpp
)

target_include_directories(
    math_core_lib PUBLIC
    ${CMAKE_CURRENT_SOURCE_DIR}/include
)

find_package(pybind11 CONFIG REQUIRED)
pybind11_add_module(equation_ast bindings.cpp)
target_link_libraries(equation_ast PRIVATE math_core_lib)

install(TARGETS equation_ast DESTINATION .)