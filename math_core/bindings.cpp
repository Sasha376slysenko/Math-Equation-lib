#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "EquationParser.hpp"

namespace py = pybind11;

PYBIND11_MODULE(equation_ast, m) {
    m.doc() = "Equation parser Python module";

    py::class_<EquationParser>(m, "EquationParser")
        .def(py::init<>())
        .def("eval_fast_cpp", &EquationParser::eval_fast_cpp, "Evaluate expression quickly")
        .def("is_valid_equation_cpp", &EquationParser::is_valid_equation_cpp, "Check if expression is valid");
}
