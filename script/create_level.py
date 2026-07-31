from math_core.python_api import equation_lib_cpp

config = equation_lib_cpp.EquationConfig(15200)
ev = equation_lib_cpp.EvalEquation(config)

ev.equation_add_sub_bracket(4)
ev.equation_add_sub_bracket(4, False)
ev.equation_add_sub_mul_div_bracket(4)