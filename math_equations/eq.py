import gc
import itertools
import operator
import random
from functools import lru_cache
from types import MappingProxyType
from typing import Iterable
from typing import Mapping, Callable
from colorama import Back, Fore, Style

"""
    Шаблони рівностей
"""
class BaseArrays:
    @staticmethod
    def add_generation_four_digit_equation(perm: tuple[str, str, str, str], ops: tuple[str, str, str, str]) -> Iterable[str]:
        yield f"{perm[0]}{ops[0]}{perm[1]}{ops[1]}{perm[2]}{ops[2]}{perm[3]}"
        yield f"({perm[0]}{ops[0]}{perm[1]}){ops[1]}{perm[2]}{ops[2]}{perm[3]}"
        yield f"{perm[0]}{ops[0]}({perm[1]}{ops[1]}{perm[2]}){ops[2]}{perm[3]}"
        yield f"{perm[0]}{ops[0]}{perm[1]}{ops[1]}({perm[2]}{ops[2]}{perm[3]})"
        yield f"({perm[0]}{ops[0]}{perm[1]}){ops[1]}({perm[2]}{ops[2]}{perm[3]})"

    @staticmethod
    def add_generation_five_digit_equation(perm: tuple[str, str, str, str, str], ops: tuple[str, str, str, str, str]) -> Iterable[str]:
        yield f"{perm[0]}{ops[0]}{perm[1]}{ops[1]}{perm[2]}{ops[2]}{perm[3]}{ops[3]}{perm[4]}"
        yield f"({perm[0]}{ops[0]}{perm[1]}){ops[1]}{perm[2]}{ops[2]}{perm[3]}{ops[3]}{perm[4]}"
        yield f"{perm[0]}{ops[0]}({perm[1]}{ops[1]}{perm[2]}){ops[2]}{perm[3]}{ops[3]}{perm[4]}"
        yield f"{perm[0]}{ops[0]}{perm[1]}{ops[1]}({perm[2]}{ops[2]}{perm[3]}){ops[3]}{perm[4]}"
        yield f"{perm[0]}{ops[0]}{perm[1]}{ops[1]}{perm[2]}{ops[2]}({perm[3]}{ops[3]}{perm[4]})"
        yield f"({perm[0]}{ops[0]}{perm[1]}){ops[1]}({perm[2]}{ops[2]}{perm[3]}){ops[3]}{perm[4]}"
        yield f"({perm[0]}{ops[0]}{perm[1]}){ops[1]}{perm[2]}{ops[2]}({perm[3]}{ops[3]}{perm[4]})"

    @staticmethod
    def add_generation_six_digit_equation(perm: tuple[str, str, str, str, str, str], ops: tuple[str, str, str, str, str, str]) -> Iterable[str]:
        yield f"{perm[0]}{ops[0]}{perm[1]}{ops[1]}{perm[2]}{ops[2]}{perm[3]}{ops[3]}{perm[4]}{ops[4]}{perm[5]}"
        yield f"({perm[0]}{ops[0]}{perm[1]}){ops[1]}{perm[2]}{ops[2]}{perm[3]}{ops[3]}{perm[4]}{ops[4]}{perm[5]}"
        yield f"{perm[0]}{ops[0]}({perm[1]}{ops[1]}{perm[2]}){ops[2]}{perm[3]}{ops[3]}{perm[4]}{ops[4]}{perm[5]}"
        yield f"{perm[0]}{ops[0]}{perm[1]}{ops[1]}({perm[2]}{ops[2]}{perm[3]}){ops[3]}{perm[4]}{ops[4]}{perm[5]}"
        yield f"{perm[0]}{ops[0]}{perm[1]}{ops[1]}{perm[2]}{ops[2]}({perm[3]}{ops[3]}{perm[4]}){ops[4]}{perm[5]}"
        yield f"{perm[0]}{ops[0]}{perm[1]}{ops[1]}{perm[2]}{ops[2]}{perm[3]}{ops[3]}({perm[4]}{ops[4]}{perm[5]})"
        yield f"({perm[0]}{ops[0]}{perm[1]}){ops[1]}({perm[2]}{ops[2]}{perm[3]}){ops[3]}{perm[4]}{ops[4]}{perm[5]}"
        yield f"({perm[0]}{ops[0]}{perm[1]}){ops[1]}{perm[2]}{ops[2]}({perm[3]}{ops[3]}{perm[4]}){ops[4]}{perm[5]}"
        yield f"({perm[0]}{ops[0]}{perm[1]}){ops[1]}{perm[2]}{ops[2]}{perm[3]}{ops[3]}({perm[4]}{ops[4]}{perm[5]})"

    @staticmethod
    def add_generation_seven_digit_equation(perm: tuple[str, str, str, str, str, str, str], ops: tuple[str, str, str, str, str, str, str]) -> Iterable[str]:
        yield f"{perm[0]}{ops[0]}{perm[1]}{ops[1]}{perm[2]}{ops[2]}{perm[3]}{ops[3]}{perm[4]}{ops[4]}{perm[5]}{ops[5]}{perm[6]}"
        yield f"({perm[0]}{ops[0]}{perm[1]}){ops[1]}{perm[2]}{ops[2]}{perm[3]}{ops[3]}{perm[4]}{ops[4]}{perm[5]}{ops[5]}{perm[6]}"
        yield f"{perm[0]}{ops[0]}({perm[1]}{ops[1]}{perm[2]}){ops[2]}{perm[3]}{ops[3]}{perm[4]}{ops[4]}{perm[5]}{ops[5]}{perm[6]}"
        yield f"{perm[0]}{ops[0]}{perm[1]}{ops[1]}({perm[2]}{ops[2]}{perm[3]}){ops[3]}{perm[4]}{ops[4]}{perm[5]}{ops[5]}{perm[6]}"
        yield f"{perm[0]}{ops[0]}{perm[1]}{ops[1]}{perm[2]}{ops[2]}({perm[3]}{ops[3]}{perm[4]}){ops[4]}{perm[5]}{ops[5]}{perm[6]}"
        yield f"{perm[0]}{ops[0]}{perm[1]}{ops[1]}{perm[2]}{ops[2]}{perm[3]}{ops[3]}({perm[4]}{ops[4]}{perm[5]}){ops[5]}{perm[6]}"
        yield f"{perm[0]}{ops[0]}{perm[1]}{ops[1]}{perm[2]}{ops[2]}{perm[3]}{ops[3]}{perm[4]}{ops[4]}({perm[5]}{ops[5]}{perm[6]})"
        yield f"({perm[0]}{ops[0]}{perm[1]}){ops[1]}({perm[2]}{ops[2]}{perm[3]}){ops[3]}{perm[4]}{ops[4]}{perm[5]}{ops[5]}{perm[6]}"
        yield f"({perm[0]}{ops[0]}{perm[1]}){ops[1]}{perm[2]}{ops[2]}({perm[3]}{ops[3]}{perm[4]}){ops[4]}{perm[5]}{ops[5]}{perm[6]}"
        yield f"({perm[0]}{ops[0]}{perm[1]}){ops[1]}{perm[2]}{ops[2]}{perm[3]}{ops[3]}({perm[4]}{ops[4]}{perm[5]}){ops[5]}{perm[6]}"
        yield f"({perm[0]}{ops[0]}{perm[1]}){ops[1]}{perm[2]}{ops[2]}{perm[3]}{ops[3]}{perm[4]}{ops[4]}({perm[5]}{ops[5]}{perm[6]})"

    @staticmethod
    def add_generation_eight_digit_equation(perm: tuple[str, str, str, str, str, str, str, str], ops: tuple[str, str, str, str, str, str, str, str]) -> Iterable[str]:
        yield f"{perm[0]}{ops[0]}{perm[1]}{ops[1]}{perm[2]}{ops[2]}{perm[3]}{ops[3]}{perm[4]}{ops[4]}{perm[5]}{ops[5]}{perm[6]}{ops[6]}{perm[7]}"
        yield f"({perm[0]}{ops[0]}{perm[1]}){ops[1]}{perm[2]}{ops[2]}{perm[3]}{ops[3]}{perm[4]}{ops[4]}{perm[5]}{ops[5]}{perm[6]}{ops[6]}{perm[7]}"
        yield f"{perm[0]}{ops[0]}({perm[1]}{ops[1]}{perm[2]}){ops[2]}{perm[3]}{ops[3]}{perm[4]}{ops[4]}{perm[5]}{ops[5]}{perm[6]}{ops[6]}{perm[7]}"
        yield f"{perm[0]}{ops[0]}{perm[1]}{ops[1]}({perm[2]}{ops[2]}{perm[3]}){ops[3]}{perm[4]}{ops[4]}{perm[5]}{ops[5]}{perm[6]}{ops[6]}{perm[7]}"
        yield f"{perm[0]}{ops[0]}{perm[1]}{ops[1]}{perm[2]}{ops[2]}({perm[3]}{ops[3]}{perm[4]}){ops[4]}{perm[5]}{ops[5]}{perm[6]}{ops[6]}{perm[7]}"
        yield f"{perm[0]}{ops[0]}{perm[1]}{ops[1]}{perm[2]}{ops[2]}{perm[3]}{ops[3]}({perm[4]}{ops[4]}{perm[5]}){ops[5]}{perm[6]}{ops[6]}{perm[7]}"
        yield f"({perm[0]}{ops[0]}{perm[1]}){ops[1]}({perm[2]}{ops[2]}{perm[3]}){ops[3]}{perm[4]}{ops[4]}{perm[5]}{ops[5]}{perm[6]}{ops[6]}{perm[7]}"
        yield f"({perm[0]}{ops[0]}{perm[1]}){ops[1]}{perm[2]}{ops[2]}({perm[3]}{ops[3]}{perm[4]}){ops[4]}{perm[5]}{ops[5]}{perm[6]}{ops[6]}{perm[7]}"
        yield f"({perm[0]}{ops[0]}{perm[1]}){ops[1]}{perm[2]}{ops[2]}{perm[3]}{ops[3]}({perm[4]}{ops[4]}{perm[5]}){ops[5]}{perm[6]}{ops[6]}{perm[7]}"
        yield f"({perm[0]}{ops[0]}{perm[1]}){ops[1]}{perm[2]}{ops[2]}{perm[3]}{ops[3]}{perm[4]}{ops[4]}({perm[5]}{ops[5]}{perm[6]}){ops[6]}{perm[7]}"
        yield f"({perm[0]}{ops[0]}{perm[1]}){ops[1]}{perm[2]}{ops[2]}{perm[3]}{ops[3]}{perm[4]}{ops[4]}{perm[5]}{ops[5]}({perm[6]}{ops[6]}{perm[7]})"


"""
    SOLID -> SRP -> EquationConfig
"""
class EquationConfig:
    __slots__ = (
        'COUNTER_ITERATION',
        'OPERATORS',
        'ADD',
        'MUL',
        'ALL',
        'ITR_ADD',
        'ITR_MUL',
        'ITR_ALL',
        'GENERATE_LEVELS_FILES'
    )

    def __init__(self, count: int) -> None:
        self.ADD: int = 1000
        self.MUL: int = 100
        self.ALL: int = 1000
        self.ITR_ADD: range = range(self.ADD)
        self.ITR_MUL: range = range(self.MUL)
        self.ITR_ALL: range = range(self.ALL)
        self.GENERATE_LEVELS_FILES: bool = True
        self.COUNTER_ITERATION: int = count
        self.OPERATORS: Mapping[str, Callable[[float, float], float]] = MappingProxyType({
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv,
            '^': operator.pow
        })


"""
    Eval_fast
"""
class EvalEquation(BaseArrays):
    __slots__ = (
        'config',
        'set_digit',
        'min_len'
    )


    def __init__(self, config: EquationConfig) -> None:
        super().__init__()
        self.config: EquationConfig = config
        self.set_digit: set[str] = {str(digit) for digit in range(5001)}
        self.min_len: int = 3


    def __del__(self) -> None:
        gc.collect()


    @staticmethod
    def _logging_operator(op="no operator") -> None:
        print("⚠️ " + Back.LIGHTRED_EX + Fore.BLACK + f"PROBLEM: op: {op}", end="")
        print(Style.RESET_ALL)


    @staticmethod
    def _logging_process_eq(marker=True) -> None:
        if marker:
            print(Back.LIGHTRED_EX + Fore.BLACK + "MAX ITERATION", end="")
            print(Style.RESET_ALL)
        else:
            print(Back.LIGHTBLUE_EX + Fore.LIGHTWHITE_EX + "CYCLE ENDED", end="")
            print(Style.RESET_ALL)


    def _toggle_variable_generate_levels_files(self):
        self.config.GENERATE_LEVELS_FILES = False


    def _create_header(self) -> None:
        if self.config.GENERATE_LEVELS_FILES:
            with open("levels.h", "w") as file:
                file.write(
                    '#pragma once\n\n'
                    '#ifndef LEVELS_H\n'
                    '#define LEVELS_H\n\n'
                    'void initAddSubBracket();\n'
                    'void initMulDivBracket();\n'
                    'void initAddSubMulDivBracket();\n\n'
                    'struct EqAddSubBracket {\n'
                    f'\tunsigned short digit[{self.config.ADD}];\n'
                    f'\tchar equation[{self.config.ADD}][1000];\n'
                    '};\n\n'
                    'struct EqMulDivBracket {\n'
                    f'\tunsigned short digit[{self.config.MUL}];\n'
                    f'\tchar equation[{self.config.MUL}][1000];\n'
                    '};\n\n'
                    'struct EqAddSubMulDivBracket {\n'
                    f'\tunsigned short digit[{self.config.ALL}];\n'
                    f'\tchar equation[{self.config.ALL}][1000];\n'
                    '};\n\n'
                    'extern struct EqAddSubBracket AddSubBracket;\n'
                    'extern struct EqMulDivBracket MulDivBracket;\n'
                    'extern struct EqAddSubMulDivBracket AddSubMulDivBracket;\n\n'
                    '#endif'
                )


    def _create_main(self) -> None:
        if self.config.GENERATE_LEVELS_FILES:
            with open("main.c", "w") as file:
                file.write(
                    '#include <stdio.h>\n'
                    '#include <string.h>\n'
                    '#include "levels.h"\n\n'
                    'extern struct EqAddSubBracket AddSubBracket;\n'
                    'extern struct EqMulDivBracket MulDivBracket;\n'
                    'extern struct EqAddSubMulDivBracket AddSubMulDivBracket;\n\n'
                    'unsigned int maxLengthOne(struct EqAddSubBracket* obj, unsigned int numberItr);\n'
                    'unsigned int maxLengthTwo(struct EqMulDivBracket* obj, unsigned int numberItr);\n'
                    'unsigned int maxLengthThree(struct EqAddSubMulDivBracket* obj, unsigned int numberItr);\n\n'
                    'int main() {\n'
                    '\t	//Length Max\n\n'
                    '\tinitAddSubBracket();\n'
                    '\tinitMulDivBracket();\n'
                    '\tinitAddSubMulDivBracket();\n\n'
                    '\tunsigned int lengthAddSubBracket;\n'
                    '\tunsigned int lengthMulDivBracket;\n'
                    '\tunsigned int lengthAddSubMulDivBracket;\n\n'
                    f'\tlengthAddSubBracket = maxLengthOne(&AddSubBracket, {self.config.ADD});\n'
                    f'\tlengthMulDivBracket = maxLengthTwo(&MulDivBracket, {self.config.MUL});\n'
                    f'\tlengthAddSubMulDivBracket = maxLengthThree(&AddSubMulDivBracket, {self.config.ALL});\n\n'
                    f'\tfloat memoryAddSubBrackets = (lengthAddSubBracket * {self.config.ADD}) / 1000.0f;\n'
                    f'\tfloat memoryMulDivBrackets = (lengthMulDivBracket * {self.config.MUL}) / 1000.0f;\n'
                    f'\tfloat memoryAddSubMulDivBracket = (lengthAddSubMulDivBracket * {self.config.ALL}) / 1000.0f;\n'
                    '\tfloat memoryTotal = memoryAddSubBrackets + memoryMulDivBrackets + memoryAddSubMulDivBracket;\n\n'
                    '\tprintf("#==================Start===================================#\\n");\n'
                    '\tprintf("Max length EqAddSubBracket: %d\\n", lengthAddSubBracket);\n'
                    '\tprintf("Max length EqMulDivBracket: %d\\n", lengthMulDivBracket);\n'
                    '\tprintf("Max length EqAddSubMulDivBracket: %d\\n", lengthAddSubMulDivBracket);\n'
                    '\tprintf("#==================End=====================================#\\n");\n\n'
                    '\tFILE* file = fopen("result_length.txt", "w");\n\n'
                    '\tif (file == NULL) {\n'
                    '\t\tprintf("File not opened!\\n");\n'
                    '\t\treturn 1;\n'
                    '\t}\n\n'
                    '\tfprintf(file, "result length: \\n");\n'
                    '\tfprintf(file, "Max length EqAddSubBracket: %d\\n", lengthAddSubBracket);\n'
                    '\tfprintf(file, "Max length EqMulDivBracket: %d\\n", lengthMulDivBracket);\n'
                    '\tfprintf(file, "Max length EqAddSubMulDivBracket: %d\\n", lengthAddSubMulDivBracket);\n'
                    '\tfprintf(file, "\\n");\n'
                    '\tfprintf(file, "Memory EqAddSubBracket(kbite): %.1f\\n", memoryAddSubBrackets);\n'
                    '\tfprintf(file, "Memory EqMulDivBracket(kbite): %.1f\\n", memoryMulDivBrackets);\n'
                    '\tfprintf(file, "Memory EqAddSubMulDivBracket(kbite): %.1f\\n", memoryAddSubMulDivBracket);\n'
                    '\tfprintf(file, "Memory total(kbite): %.1f\\n", memoryTotal);\n'
                    '\tfclose(file);\n\n'
                    '\treturn 0;\n'
                    '}\n\n'
                    'unsigned int maxLengthOne(struct EqAddSubBracket *obj, unsigned int numberItr) {\n'
                    '\tint lengthEq = 0;\n'
                    '\tfor (int i = 0; i < numberItr; i++) {\n'
                    '\t\tif (strlen(obj->equation[i]) > lengthEq)\n'
                    '\t\t\tlengthEq = strlen(obj->equation[i]);\n'
                    '\t}\n'
                    '\treturn lengthEq;\n'
                    '}\n\n'
                    'unsigned int maxLengthTwo(struct EqMulDivBracket* obj, unsigned int numberItr) {\n'
                    '\tint lengthEq = 0;\n'
                    '\tfor (int i = 0; i < numberItr; i++) {\n'
                    '\t\tif (strlen(obj->equation[i]) > lengthEq)\n'
                    '\t\t\tlengthEq = strlen(obj->equation[i]);\n'
                    '\t}\n'
                    '\treturn lengthEq;\n'
                    '}\n\n'
                    'unsigned int maxLengthThree(struct EqAddSubMulDivBracket* obj, unsigned int numberItr) {\n'
                    '\tint lengthEq = 0;\n'
                    '\tfor (int i = 0; i < numberItr; i++) {\n'
                    '\t\tif (strlen(obj->equation[i]) > lengthEq)\n'
                    '\t\t\tlengthEq = strlen(obj->equation[i]);\n'
                    '\t}\n'
                    '\treturn lengthEq;\n'
                    '}'
                )


    def _create_pyx(self) -> None:
        if self.config.GENERATE_LEVELS_FILES:
            with open("equation_levels.pyx", "w") as file:
                file.write(
                    "cdef set SYMBOL_IF = {\n"
                    "\t'*', '/', '+', '-', '(', ')', '=',\n"
                    "\t'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'\n"
                    '}\n\n'
                    'cdef extern from "levels.h":\n'
                    '\tcdef struct EqAddSubBracket:\n'
                    f'\t\tunsigned short digit[{self.config.ADD}]\n'
                    f'\t\tchar equation[{self.config.ADD}][1000]\n\n'
                    '\tcdef struct EqMulDivBracket:\n'
                    f'\t\tunsigned short digit[{self.config.MUL}]\n'
                    f'\t\tchar equation[{self.config.MUL}][1000]\n\n'
                    '\tcdef struct EqAddSubMulDivBracket:\n'
                    f'\t\tunsigned short digit[{self.config.ALL}]\n'
                    f'\t\tchar equation[{self.config.ALL}][1000]\n\n'
                    '\tcdef void initAddSubBracket()\n'
                    '\tcdef void initMulDivBracket()\n'
                    '\tcdef void initAddSubMulDivBracket()\n\n'
                    '\tcdef EqAddSubBracket AddSubBracket\n'
                    '\tcdef EqMulDivBracket MulDivBracket\n'
                    '\tcdef EqAddSubMulDivBracket AddSubMulDivBracket\n\n\n'
                    'def init():\n'
                    '\tinitAddSubBracket()\n'
                    '\tinitMulDivBracket()\n'
                    '\tinitAddSubMulDivBracket()\n\n\n'
                    'def list_eq(str eqs_i):\n'
                    "\tcdef str ch = ''\n"
                    "\tcdef str temp_str = ''\n"
                    '\tcdef list result_eq = []\n\n'
                    '\tfor ch in eqs_i:\n'
                    '\t\tif ch in SYMBOL_IF:\n'
                    '\t\t\ttemp_str += ch\n'
                    "\t\telif ch == ',':\n"
                    '\t\t\tresult_eq.append(temp_str)\n'
                    '\t\telse:\n'
                    "\t\t\ttemp_str = ''\n"
                    '\treturn result_eq\n\n\n'
                    'def get_digit_add_sub_br(unsigned int index):\n'
                    '\treturn AddSubBracket.digit[index]\n\n\n'
                    'cpdef get_eq_add_sub_br(unsigned int index):\n'
                    "\tcdef str eqs = bytes(AddSubBracket.equation[index]).decode('utf-8')\n"
                    '\treturn list_eq(eqs)\n\n\n'
                    'def get_digit_mul_div_br(unsigned int index):\n'
                    '\treturn MulDivBracket.digit[index]\n\n\n'
                    'cpdef get_eq_mul_div_br(unsigned int index):\n'
                    "\tcdef str eqs = bytes(MulDivBracket.equation[index]).decode('utf-8')\n"
                    '\treturn list_eq(eqs)\n\n\n'
                    'def get_digit_add_sub_mul_div_br(unsigned int index):\n'
                    '\treturn AddSubMulDivBracket.digit[index]\n\n\n'
                    'cpdef get_eq_add_sub_mul_div_br(unsigned int index):\n'
                    "\tcdef str eqs = bytes(AddSubMulDivBracket.equation[index]).decode('utf-8')\n"
                    '\treturn list_eq(eqs)'
                )


    def _create_setup(self)-> None:
        if self.config.GENERATE_LEVELS_FILES:
            with open("../setup_levels.py", "w") as file:
                file.write(
                    'from setuptools import setup, Extension\n'
                    'from Cython.Build import cythonize\n\n'
                    'extension = [\n'
                    '\tExtension(\n'
                    "\t\t'equation_levels',\n"
                    '\t\tsources=[\n'
                    "\t\t\t'equation_levels.pyx',\n"
                    "\t\t\t'eq_add_sub_br.c',\n"
                    "\t\t\t'eq_mul_div_br.c',\n"
                    "\t\t\t'eq_add_sub_mul_div_br.c'\n"
                    '\t\t],\n'
                    "\t\tinclude_dirs=['.']\n"
                    '\t)\n'
                    ']\n\n'
                    "setup(name='equation_levels', ext_modules=cythonize(extension, language_level='3'))"
                )


    @staticmethod
    def _create_add_sub_bracket() -> None:
        with open("eq_add_sub_br.c", "w") as file:
            file.write("#include \"levels.h\"\n")
            file.write("#include <string.h>")
            file.write("\n\n")
            file.write("struct EqAddSubBracket AddSubBracket;\n")
            file.write("\n")


    @staticmethod
    def _create_mul_div_bracket() -> None:
        with open("eq_mul_div_br.c", "w") as file:
            file.write("#include \"levels.h\"\n")
            file.write("#include <string.h>")
            file.write("\n\n")
            file.write("struct EqMulDivBracket MulDivBracket;\n")
            file.write("\n")


    @staticmethod
    def _create_add_sub_mul_div_bracket() -> None:
        with open("eq_add_sub_mul_div_br.c", "w") as file:
            file.write("#include \"levels.h\"\n")
            file.write("#include <string.h>")
            file.write("\n\n")
            file.write("struct EqAddSubMulDivBracket AddSubMulDivBracket;\n")
            file.write("\n")


    @staticmethod
    def _file_init(i_itr: int, res_eq: tuple[str, set[str]], f_name: str, str_name: str, op_counter) -> None:
        res_str: str = ''

        for j, eq in  enumerate(res_eq[1]):
            if j != len(res_eq[1]) - 1:
                res_str += eq + ', '
            else:
                res_str += eq

        with open(f_name, "a") as file:
            if i_itr == 0:
                file.write(f"void init{str_name}() {{\n")

            file.write(f"\t{str_name}.digit[{i_itr}] = {int(res_eq[0])};\n")
            file.write(f'\tstrcpy({str_name}.equation[{i_itr}], "{res_str}");\n')

            if i_itr == op_counter - 1:
                file.write("}")
            if i_itr != op_counter - 1:
                file.write("\n")


    @lru_cache(maxsize=10000)
    def is_valid_equation(self, equation: str) -> bool:
        left: str
        right: str
        left_value: float
        right_value: float

        left, right = equation.split('=')
        try:
            left = left.replace('^', '**')
            right = right.replace('^', '**')
            left_value = eval(left)
            right_value = eval(right)
        except Exception:
            return False
        return left_value != 0.0 and right_value != 0.0 and left_value == right_value


    @staticmethod
    def _sorted_eqs(eqs: list[str]) -> set[str]:
        remove_equations: set[str] = set()

        eq: str
        eq_bracket_1: str
        eq_bracket_2: str
        eq_bracket_3: str
        eq_bracket_4: str
        eq_bracket_5: str
        eq_bracket_6: str

        for eq in eqs:
            if not eq:
                continue
            if '(' not in eq:
                left_eq, right_eq = eq.split('=')

                eq_bracket_1 = f"({left_eq})=({right_eq})"
                eq_bracket_2 = f"({right_eq})=({left_eq})"
                eq_bracket_3 = f"{right_eq}=({left_eq})"
                eq_bracket_4 = f"({right_eq})={left_eq}"
                eq_bracket_5 = f"({left_eq})={right_eq}"
                eq_bracket_6 = f"{left_eq}=({right_eq})"

                remove_equations.add(eq_bracket_1)
                remove_equations.add(eq_bracket_2)
                remove_equations.add(eq_bracket_3)
                remove_equations.add(eq_bracket_4)
                remove_equations.add(eq_bracket_5)
                remove_equations.add(eq_bracket_6)
        eqs_result: set[str] = {eq for eq in eqs if eq not in remove_equations}
        return eqs_result


    def _check_expression(self, expression_tuple: tuple[str, int]) -> str:
        expr: str
        index: int
        counter_symbol: int = 0
        expr_result: str = ''
        symbol: str
        expr, index = expression_tuple

        if {'('} & set(expr):
            counter: int = 0
            flag: bool = True
            index_bracket_1: int = 0
            index_bracket_2: int = 0

            for symbol in expr:
                if{'+', '-', '*', '/', '^'} & set(symbol):
                    counter += 1
                elif symbol == '(':
                    if flag:
                        index_bracket_1 = counter + 1
                        flag = False
                    else:
                        index_bracket_2 = counter + 1
            if index_bracket_1 == index or index_bracket_2 == index:
                return ""

        if expr[0] == '-' and index == 1:
            return ""

        for symbol in expr:
            if {'+', '-', '*', '/', '^'} & set(symbol):
                counter_symbol += 1
                if counter_symbol == index:
                    expr_result += '='
                else:
                    expr_result += symbol
            else:
                expr_result += symbol
        if self.is_valid_equation(expr_result):
            return expr_result
        return ""


    def process_equation_one(self, digit: str) -> str | None:
        number_len: int = len(digit)
        counter: int = 0
        expr: str  # noqa: F842
        eq_pos: int  # noqa: F842
        result: str
        tasks: list[tuple[str, int]]
        results: list[str]

        perm_list_4: Iterable[tuple[str, ...]]
        perm_list_5: Iterable[tuple[str, ...]]
        perm_list_6: Iterable[tuple[str, ...]]
        perm_list_7: Iterable[tuple[str, ...]]
        perm_list_8: Iterable[tuple[str, ...]]

        ops_list_4: Iterable[tuple[str, ...]]
        ops_list_5: Iterable[tuple[str, ...]]
        ops_list_6: Iterable[tuple[str, ...]]
        ops_list_7: Iterable[tuple[str, ...]]
        ops_list_8: Iterable[tuple[str, ...]]

        match number_len:
            case 4:
                perm_list_4 = itertools.permutations(digit)
                ops_list_4 = itertools.product(self.config.OPERATORS.keys(), repeat=number_len)

                for perm in perm_list_4:
                    for ops in ops_list_4:
                        if counter == self.config.COUNTER_ITERATION:
                            self._logging_process_eq()
                            return ""

                        unique_expr = set(BaseArrays.add_generation_four_digit_equation(perm, ops)) # type: ignore
                        tasks = [(expr, eq_pos) for expr in unique_expr for eq_pos in range(1, 4)]
                        results = [self._check_expression(task) for task in tasks]
                        for result in results:
                            if result:
                                return result
                        counter += 1
            case 5:
                perm_list_5 = itertools.permutations(digit)
                ops_list_5 = itertools.product(self.config.OPERATORS.keys(), repeat=number_len)

                for perm in perm_list_5:
                    for ops in ops_list_5:
                        if counter == self.config.COUNTER_ITERATION:
                            self._logging_process_eq()
                            return ""

                        unique_expr = set(BaseArrays.add_generation_five_digit_equation(perm, ops)) # type: ignore
                        tasks = [(expr, eq_pos) for expr in unique_expr for eq_pos in range(1, 5)]
                        results = [self._check_expression(task) for task in tasks]
                        for result in results:
                            if result:
                                return result
                        counter += 1
            case 6:
                perm_list_6 = itertools.permutations(digit)
                ops_list_6 = itertools.product(self.config.OPERATORS.keys(), repeat=number_len)

                for perm in perm_list_6:
                    for ops in ops_list_6:
                        if counter == self.config.COUNTER_ITERATION:
                            self._logging_process_eq()
                            return ""

                        unique_expr = set(BaseArrays.add_generation_six_digit_equation(perm, ops)) # type: ignore
                        tasks = [(expr, eq_pos) for expr in unique_expr for eq_pos in range(1, 6)]
                        results = [self._check_expression(task) for task in tasks]
                        for result in results:
                            if result:
                                return result
                        counter += 1
            case 7:
                perm_list_7 = itertools.permutations(digit)
                ops_list_7 = itertools.product(self.config.OPERATORS.keys(), repeat=number_len)

                for perm in perm_list_7:
                    for ops in ops_list_7:
                        if counter == self.config.COUNTER_ITERATION:
                            self._logging_process_eq()
                            return ""

                        unique_expr = set(BaseArrays.add_generation_seven_digit_equation(perm, ops)) # type: ignore
                        tasks = [(expr, eq_pos) for expr in unique_expr for eq_pos in range(1, 7)]
                        results = [self._check_expression(task) for task in tasks]
                        for result in results:
                            if result:
                                return result
                        counter += 1
            case 8:
                perm_list_8 = itertools.permutations(digit)
                ops_list_8 = itertools.product(self.config.OPERATORS.keys(), repeat=number_len)

                for perm in perm_list_8:
                    for ops in ops_list_8:
                        if counter == self.config.COUNTER_ITERATION:
                            self._logging_process_eq()
                            return ""

                        unique_expr = set(BaseArrays.add_generation_eight_digit_equation(perm, ops)) # type: ignore
                        tasks = [(expr, eq_pos) for expr in unique_expr for eq_pos in range(1, 8)]
                        results = [self._check_expression(task) for task in tasks]
                        for result in results:
                            if result:
                                return result
                        counter += 1
        self._logging_process_eq(False)
        return None


    def process_equation_all_possible(self, digit: str, flag_sorted: bool=False) -> list[str] | None:
        number_len: int = len(digit)
        counter: int = 0

        expr: str  # noqa: F842
        eq_pos: int  # noqa: F842
        unique_expr: set[str]
        tasks: list[tuple[str, int]]
        results: list[str]
        result: str
        set_equation_result: set[str] = set()

        perm_list_4: Iterable[tuple[str, ...]]
        perm_list_5: Iterable[tuple[str, ...]]
        perm_list_6: Iterable[tuple[str, ...]]
        perm_list_7: Iterable[tuple[str, ...]]
        perm_list_8: Iterable[tuple[str, ...]]

        ops_list_4: Iterable[tuple[str, ...]]
        ops_list_5: Iterable[tuple[str, ...]]
        ops_list_6: Iterable[tuple[str, ...]]
        ops_list_7: Iterable[tuple[str, ...]]
        ops_list_8: Iterable[tuple[str, ...]]

        match number_len:
            case 4:
                perm_list_4 = itertools.permutations(digit)
                ops_list_4 = itertools.product(self.config.OPERATORS.keys(), repeat=number_len)

                for perm in perm_list_4:
                    for ops in ops_list_4:
                        if counter == self.config.COUNTER_ITERATION:
                            self._logging_process_eq()
                            return list(set_equation_result)

                        unique_expr = set(BaseArrays.add_generation_four_digit_equation(perm, ops)) # type: ignore
                        tasks = [(expr, eq_pos) for expr in unique_expr for eq_pos in range(1, 4)]
                        results = [self._check_expression(task) for task in tasks]
                        for result in results:
                            if result:
                                set_equation_result.add(result)
                        counter += 1
            case 5:
                perm_list_5 = itertools.permutations(digit)
                ops_list_5 = itertools.product(self.config.OPERATORS.keys(), repeat=number_len)

                for perm in perm_list_5:
                    for ops in ops_list_5:
                        if counter == self.config.COUNTER_ITERATION:
                            self._logging_process_eq()
                            return list(set_equation_result)

                        unique_expr = set(BaseArrays.add_generation_five_digit_equation(perm, ops)) # type: ignore
                        tasks = [(expr, eq_pos) for expr in unique_expr for eq_pos in range(1, 5)]
                        results = [self._check_expression(task) for task in tasks]
                        for result in results:
                            if result:
                                set_equation_result.add(result)
                        counter += 1
            case 6:
                perm_list_6 = itertools.permutations(digit)
                ops_list_6 = itertools.product(self.config.OPERATORS.keys(), repeat=number_len)

                for perm in perm_list_6:
                    for ops in ops_list_6:
                        if counter == self.config.COUNTER_ITERATION:
                            self._logging_process_eq()
                            return list(set_equation_result)

                        unique_expr = set(BaseArrays.add_generation_six_digit_equation(perm, ops)) # type: ignore
                        tasks = [(expr, eq_pos) for expr in unique_expr for eq_pos in range(1, 6)]
                        results = [self._check_expression(task) for task in tasks]
                        for result in results:
                            if result:
                                set_equation_result.add(result)
                        counter += 1
            case 7:
                perm_list_7 = itertools.permutations(digit)
                ops_list_7 = itertools.product(self.config.OPERATORS.keys(), repeat=number_len)

                for perm in perm_list_7:
                    for ops in ops_list_7:
                        if counter == self.config.COUNTER_ITERATION:
                            self._logging_process_eq()
                            return list(set_equation_result)

                        unique_expr = set(BaseArrays.add_generation_seven_digit_equation(perm, ops)) # type: ignore
                        tasks = [(expr, eq_pos) for expr in unique_expr for eq_pos in range(1, 7)]
                        results = [self._check_expression(task) for task in tasks]
                        for result in results:
                            if result:
                                set_equation_result.add(result)
                        counter += 1
            case 8:
                perm_list_8 = itertools.permutations(digit)
                ops_list_8 = itertools.product(self.config.OPERATORS.keys(), repeat=number_len)

                for perm in perm_list_8:
                    for ops in ops_list_8:
                        if counter == self.config.COUNTER_ITERATION:
                            self._logging_process_eq()
                            return list(set_equation_result)

                        unique_expr = set(BaseArrays.add_generation_eight_digit_equation(perm, ops)) # type: ignore
                        tasks = [(expr, eq_pos) for expr in unique_expr for eq_pos in range(1, 8)]
                        results = [self._check_expression(task) for task in tasks]
                        for result in results:
                            if result:
                                set_equation_result.add(result)
                        counter += 1

        if flag_sorted:
            set_equation_result = self._sorted_eqs(list(set_equation_result))
        self._logging_process_eq(False)
        return list(set_equation_result)


    def equation_add_sub_bracket(self, number_len: int, flag_add_sub=True) -> None:
        res_tup: tuple[str, set[str]]
        set_unique: set[str] = set()
        self._create_header()
        self._create_main()
        self._create_pyx()
        self._create_setup()
        self._toggle_variable_generate_levels_files()

        if flag_add_sub:
            self._create_add_sub_bracket()
        else:
            self._create_mul_div_bracket()


        def process_eq() -> tuple[str, set[str]]:
            nonlocal number_len

            counter: int = 0
            digit: str = ''
            expr: str  # noqa: F842
            eq_pos: int  # noqa: F842
            unique_expr: set[str]
            tasks: list[tuple[str, int]]
            results: list[str]
            result: str
            set_equation_result: set[str] = set()

            ops_list_4: Iterable[tuple[str, ...]]
            ops_list_5: Iterable[tuple[str, ...]]
            ops_list_6: Iterable[tuple[str, ...]]
            ops_list_7: Iterable[tuple[str, ...]]
            ops_list_8: Iterable[tuple[str, ...]]

            perm_list_4: Iterable[tuple[str, ...]]
            perm_list_5: Iterable[tuple[str, ...]]
            perm_list_6: Iterable[tuple[str, ...]]
            perm_list_7: Iterable[tuple[str, ...]]
            perm_list_8: Iterable[tuple[str, ...]]

            match number_len:
                case 4:
                    digit = str(random.randint(1000, 9999))
                    perm_list_4 = itertools.permutations(digit)

                    if flag_add_sub:
                        ops_list_4 = itertools.product(['+', '-'], repeat=number_len)
                    else:
                        ops_list_4 = itertools.product(['*', '/'], repeat=number_len)

                    for perm in perm_list_4:
                        for ops in ops_list_4:
                            if counter == self.config.COUNTER_ITERATION:
                                self._logging_process_eq()
                                set_equation_result = self._sorted_eqs(list(set_equation_result))
                                return digit, set_equation_result

                            unique_expr = set(BaseArrays.add_generation_four_digit_equation(perm, ops)) # type: ignore
                            tasks = [(expr, eq_pos) for expr in unique_expr for eq_pos in range(1, 4)]
                            results = [self._check_expression(task) for task in tasks]
                            for result in results:
                                if result:
                                    set_equation_result.add(result)
                            counter += 1
                case 5:
                    digit = str(random.randint(10000, 99999))
                    perm_list_5 = itertools.permutations(digit)

                    if flag_add_sub:
                        ops_list_5 = itertools.product(['+', '-'], repeat=number_len)
                    else:
                        ops_list_5 = itertools.product(['*', '/'], repeat=number_len)

                    for perm in perm_list_5:
                        for ops in ops_list_5:
                            if counter == self.config.COUNTER_ITERATION:
                                self._logging_process_eq()
                                set_equation_result = self._sorted_eqs(list(set_equation_result))
                                return digit, set_equation_result

                            unique_expr = set(BaseArrays.add_generation_five_digit_equation(perm, ops)) # type: ignore
                            tasks = [(expr, eq_pos) for expr in unique_expr for eq_pos in range(1, 5)]
                            results = [self._check_expression(task) for task in tasks]
                            for result in results:
                                if result:
                                    set_equation_result.add(result)
                            counter += 1
                case 6:
                    digit = str(random.randint(100000, 999999))
                    perm_list_6 = itertools.permutations(digit)

                    if flag_add_sub:
                        ops_list_6 = itertools.product(['+', '-'], repeat=number_len)
                    else:
                        ops_list_6 = itertools.product(['*', '/'], repeat=number_len)

                    for perm in perm_list_6:
                        for ops in ops_list_6:
                            if counter == self.config.COUNTER_ITERATION:
                                self._logging_process_eq()
                                set_equation_result = self._sorted_eqs(list(set_equation_result))
                                return digit, set_equation_result

                            unique_expr = set(BaseArrays.add_generation_six_digit_equation(perm, ops)) # type: ignore
                            tasks = [(expr, eq_pos) for expr in unique_expr for eq_pos in range(1, 6)]
                            results = [self._check_expression(task) for task in tasks]
                            for result in results:
                                if result:
                                    set_equation_result.add(result)
                            counter += 1
                case 7:
                    digit = str(random.randint(1000000, 9999999))
                    perm_list_7 = itertools.permutations(digit)

                    if flag_add_sub:
                        ops_list_7 = itertools.product(['+', '-'], repeat=number_len)
                    else:
                        ops_list_7 = itertools.product(['*', '/'], repeat=number_len)

                    for perm in perm_list_7:
                        for ops in ops_list_7:
                            if counter == self.config.COUNTER_ITERATION:
                                self._logging_process_eq()
                                set_equation_result = self._sorted_eqs(list(set_equation_result))
                                return digit, set_equation_result

                            unique_expr = set(BaseArrays.add_generation_seven_digit_equation(perm, ops)) # type: ignore
                            tasks = [(expr, eq_pos) for expr in unique_expr for eq_pos in range(1, 7)]
                            results = [self._check_expression(task) for task in tasks]
                            for result in results:
                                if result:
                                    set_equation_result.add(result)
                            counter += 1
                case 8:
                    digit = str(random.randint(10000000, 99999999))
                    perm_list_8 = itertools.permutations(digit)

                    if flag_add_sub:
                        ops_list_8 = itertools.product(['+', '-'], repeat=number_len)
                    else:
                        ops_list_8 = itertools.product(['*', '/'], repeat=number_len)

                    for perm in perm_list_8:
                        for ops in ops_list_8:
                            if counter == self.config.COUNTER_ITERATION:
                                self._logging_process_eq()
                                set_equation_result = self._sorted_eqs(list(set_equation_result))
                                return digit, set_equation_result

                            unique_expr = set(BaseArrays.add_generation_eight_digit_equation(perm, ops)) # type: ignore
                            tasks = [(expr, eq_pos) for expr in unique_expr for eq_pos in range(1, 8)]
                            results = [self._check_expression(task) for task in tasks]
                            for result in results:
                                if result:
                                    set_equation_result.add(result)
                            counter += 1
            return digit, set_equation_result


        if flag_add_sub:
            for i in self.config.ITR_ADD:
                while True:
                    res_tup = process_eq()
                    if len(res_tup[1]) >= self.min_len and res_tup[0] not in set_unique:
                        set_unique.add(res_tup[0])
                        break
                self._file_init(
                    i,
                    res_tup,
                    'eq_add_sub_br.c',
                    'AddSubBracket',
                    self.config.ADD
                )
        else:
            for i in self.config.ITR_MUL:
                while True:
                    res_tup = process_eq()
                    if len(res_tup[1]) >= self.min_len and res_tup[0] not in set_unique:
                        set_unique.add(res_tup[0])
                        break
                self._file_init(
                    i,
                    res_tup,
                    'eq_mul_div_br.c',
                    'MulDivBracket',
                    self.config.MUL
                )
        self._logging_process_eq(False)


    def equation_add_sub_mul_div_bracket(self, number_len: int) -> None:
        res_tup: tuple[str, set[str]]
        set_unique: set[str] = set()
        self._create_header()
        self._create_main()
        self._create_pyx()
        self._create_setup()
        self._toggle_variable_generate_levels_files()
        self._create_add_sub_mul_div_bracket()


        def process_eq() -> tuple[str, set[str]]:
            nonlocal number_len

            counter: int = 0
            digit: str = ''
            expr: str  # noqa: F842
            eq_pos: int  # noqa: F842
            unique_expr: set[str]
            tasks: list[tuple[str, int]]
            results: list[str]
            result: str
            set_equation_result: set[str] = set()

            perm_list_4: Iterable[tuple[str, ...]]
            perm_list_5: Iterable[tuple[str, ...]]
            perm_list_6: Iterable[tuple[str, ...]]
            perm_list_7: Iterable[tuple[str, ...]]
            perm_list_8: Iterable[tuple[str, ...]]

            ops_list_4: Iterable[tuple[str, ...]]
            ops_list_5: Iterable[tuple[str, ...]]
            ops_list_6: Iterable[tuple[str, ...]]
            ops_list_7: Iterable[tuple[str, ...]]
            ops_list_8: Iterable[tuple[str, ...]]

            match number_len:
                case 4:
                    digit = str(random.randint(1000, 9999))
                    perm_list_4 = itertools.permutations(digit)
                    ops_list_4 = itertools.product(['*', '/', '+', '-'], repeat=number_len)

                    for perm in perm_list_4:
                        for ops in ops_list_4:
                            if counter == self.config.COUNTER_ITERATION:
                                self._logging_process_eq()
                                set_equation_result = self._sorted_eqs(list(set_equation_result))
                                return digit, set_equation_result

                            unique_expr = set(BaseArrays.add_generation_four_digit_equation(perm, ops)) # type: ignore
                            tasks = [(expr, eq_pos) for expr in unique_expr for eq_pos in range(1, 4)]
                            results = [self._check_expression(task) for task in tasks]
                            for result in results:
                                if result:
                                    set_equation_result.add(result)
                            counter += 1
                case 5:
                    digit = str(random.randint(10000, 99999))
                    perm_list_5 = itertools.permutations(digit)
                    ops_list_5 = itertools.product(['*', '/', '+', '-'], repeat=number_len)

                    for perm in perm_list_5:
                        for ops in ops_list_5:
                            if counter == self.config.COUNTER_ITERATION:
                                self._logging_process_eq()
                                set_equation_result = self._sorted_eqs(list(set_equation_result))
                                return digit, set_equation_result

                            unique_expr = set(BaseArrays.add_generation_five_digit_equation(perm, ops)) # type: ignore
                            tasks = [(expr, eq_pos) for expr in unique_expr for eq_pos in range(1, 5)]
                            results = [self._check_expression(task) for task in tasks]
                            for result in results:
                                if result:
                                    set_equation_result.add(result)
                            counter += 1
                case 6:
                    digit = str(random.randint(100000, 999999))
                    perm_list_6 = itertools.permutations(digit)
                    ops_list_6 = itertools.product(['*', '/', '+', '-'], repeat=number_len)

                    for perm in perm_list_6:
                        for ops in ops_list_6:
                            if counter == self.config.COUNTER_ITERATION:
                                self._logging_process_eq()
                                set_equation_result = self._sorted_eqs(list(set_equation_result))
                                return digit, set_equation_result

                            unique_expr = set(BaseArrays.add_generation_six_digit_equation(perm, ops)) # type: ignore
                            tasks = [(expr, eq_pos) for expr in unique_expr for eq_pos in range(1, 6)]
                            results = [self._check_expression(task) for task in tasks]
                            for result in results:
                                if result:
                                    set_equation_result.add(result)
                            counter += 1
                case 7:
                    digit = str(random.randint(1000000, 9999999))
                    perm_list_7 = itertools.permutations(digit)
                    ops_list_7 = itertools.product(['*', '/', '+', '-'], repeat=number_len)

                    for perm in perm_list_7:
                        for ops in ops_list_7:
                            if counter == self.config.COUNTER_ITERATION:
                                self._logging_process_eq()
                                set_equation_result = self._sorted_eqs(list(set_equation_result))
                                return digit, set_equation_result

                            unique_expr = set(BaseArrays.add_generation_seven_digit_equation(perm, ops)) # type: ignore
                            tasks = [(expr, eq_pos) for expr in unique_expr for eq_pos in range(1, 7)]
                            results = [self._check_expression(task) for task in tasks]
                            for result in results:
                                if result:
                                    set_equation_result.add(result)
                            counter += 1
                case 8:
                    digit = str(random.randint(10000000, 99999999))
                    perm_list_8 = itertools.permutations(digit)
                    ops_list_8 = itertools.product(['*', '/', '+', '-'], repeat=number_len)

                    for perm in perm_list_8:
                        for ops in ops_list_8:
                            if counter == self.config.COUNTER_ITERATION:
                                self._logging_process_eq()
                                set_equation_result = self._sorted_eqs(list(set_equation_result))
                                return digit, set_equation_result

                            unique_expr = set(BaseArrays.add_generation_eight_digit_equation(perm, ops)) # type: ignore
                            tasks = [(expr, eq_pos) for expr in unique_expr for eq_pos in range(1, 8)]
                            results = [self._check_expression(task) for task in tasks]
                            for result in results:
                                if result:
                                    set_equation_result.add(result)
                            counter += 1
            return digit, set_equation_result


        for i in self.config.ITR_ALL:
            while True:
                res_tup = process_eq()
                if len(res_tup[1]) >= self.min_len and res_tup[0] not in set_unique:
                    set_unique.add(res_tup[0])
                    break
            self._file_init(i, res_tup, 'eq_add_sub_mul_div_br.c', 'AddSubMulDivBracket', self.config.ALL)
        self._logging_process_eq(False)


if __name__ == "__main__":
    object_config = EquationConfig(15200)
    ev = EvalEquation(object_config)
    print(ev.process_equation_all_possible('12345678'))