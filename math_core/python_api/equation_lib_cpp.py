import os
import gc
import itertools
import operator
import random
import logging

import equation_ast
from pathlib import Path
from types import MappingProxyType
from typing import Iterable
from typing import Mapping, Callable


"""
+-------------------------+
//------ 15.09.2025 -----//
|=== Шаблони рівностей ===|
+-------------------------+
"""
class BaseArrays:
    @staticmethod
    def add_generation_four_digit_equation(perm: tuple[str, str, str, str],
                                           ops: tuple[str, str, str, str]) -> Iterable[str]:
        yield f"{perm[0]}{ops[0]}{perm[1]}{ops[1]}{perm[2]}{ops[2]}{perm[3]}"
        yield f"({perm[0]}{ops[0]}{perm[1]}){ops[1]}{perm[2]}{ops[2]}{perm[3]}"
        yield f"{perm[0]}{ops[0]}({perm[1]}{ops[1]}{perm[2]}){ops[2]}{perm[3]}"
        yield f"{perm[0]}{ops[0]}{perm[1]}{ops[1]}({perm[2]}{ops[2]}{perm[3]})"
        yield f"({perm[0]}{ops[0]}{perm[1]}){ops[1]}({perm[2]}{ops[2]}{perm[3]})"

    @staticmethod
    def add_generation_five_digit_equation(perm: tuple[str, str, str, str, str],
                                           ops: tuple[str, str, str, str, str]) -> Iterable[str]:
        yield f"{perm[0]}{ops[0]}{perm[1]}{ops[1]}{perm[2]}{ops[2]}{perm[3]}{ops[3]}{perm[4]}"
        yield f"({perm[0]}{ops[0]}{perm[1]}){ops[1]}{perm[2]}{ops[2]}{perm[3]}{ops[3]}{perm[4]}"
        yield f"{perm[0]}{ops[0]}({perm[1]}{ops[1]}{perm[2]}){ops[2]}{perm[3]}{ops[3]}{perm[4]}"
        yield f"{perm[0]}{ops[0]}{perm[1]}{ops[1]}({perm[2]}{ops[2]}{perm[3]}){ops[3]}{perm[4]}"
        yield f"{perm[0]}{ops[0]}{perm[1]}{ops[1]}{perm[2]}{ops[2]}({perm[3]}{ops[3]}{perm[4]})"
        yield f"({perm[0]}{ops[0]}{perm[1]}){ops[1]}({perm[2]}{ops[2]}{perm[3]}){ops[3]}{perm[4]}"
        yield f"({perm[0]}{ops[0]}{perm[1]}){ops[1]}{perm[2]}{ops[2]}({perm[3]}{ops[3]}{perm[4]})"

    @staticmethod
    def add_generation_six_digit_equation(perm: tuple[str, str, str, str, str, str],
                                          ops: tuple[str, str, str, str, str, str]) -> Iterable[str]:
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
    def add_generation_seven_digit_equation(perm: tuple[str, str, str, str, str, str, str],
                                            ops: tuple[str, str, str, str, str, str, str]) -> Iterable[str]:
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
    def add_generation_eight_digit_equation(perm: tuple[str, str, str, str, str, str, str, str],
                                            ops: tuple[str, str, str, str, str, str, str, str]) -> Iterable[str]:
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
+-------------------------------+
//-------- 15.09.2025 ---------//
|SOLID -> SRP -> EquationConfig |
+-------------------------------+
"""
class EquationConfig:
    __slots__ = (
        'ADD',
        'MUL',
        'ALL',
        'EQ_4',
        'EQ_5',
        'EQ_6',
        'EQ_7',
        'EQ_8',
        'EQ_N_LW_4',
        'EQ_N_LW_5',
        'EQ_N_LW_6',
        'EQ_N_LW_7',
        'EQ_N_LW_8',
        'ITR_ADD',
        'ITR_MUL',
        'ITR_ALL',
        'ITR_EQ_4',
        'ITR_EQ_5',
        'ITR_EQ_6',
        'ITR_EQ_7',
        'ITR_EQ_8',
        'GENERATE_LEVELS_FILES',
        'COUNTER_ITERATION',
        'BASE_DIR',
        'INCLUDE_DIR',
        'HEADER',
        'HEADER_EQ',
        'MAIN',
        'MAIN_EQ',
        'PYX',
        'PYX_EQ',
        'SETUP',
        'SETUP_EQ',
        'ADD_SUB_BR',
        'MUL_DIV_BR',
        'ADD_SUB_MUL_DIV_BR',
        'INCLUDE_EQ_4',
        'INCLUDE_EQ_5',
        'INCLUDE_EQ_6',
        'INCLUDE_EQ_7',
        'INCLUDE_EQ_8',
        'OPERATORS'
    )


    def __init__(self, count: int) -> None:
        # INT MAX -> ELEMENT STRUCT -> ELEMENT ARRAY
        self.ADD: int = 1900
        self.MUL: int = 600
        self.ALL: int = 1900
        self.EQ_4: int = 10
        self.EQ_5: int = 10
        self.EQ_6: int = 10
        self.EQ_7: int = 10
        self.EQ_8: int = 10

        # STR EQ
        self.EQ_N_LW_4: str = 'eq_4'
        self.EQ_N_LW_5: str = 'eq_5'
        self.EQ_N_LW_6: str = 'eq_6'
        self.EQ_N_LW_7: str = 'eq_7'
        self.EQ_N_LW_8: str = 'eq_8'

        # ITERABLE OBJECTS
        self.ITR_ADD: range = range(self.ADD)
        self.ITR_MUL: range = range(self.MUL)
        self.ITR_ALL: range = range(self.ALL)
        self.ITR_EQ_4: range = range(self.EQ_4)
        self.ITR_EQ_5: range = range(self.EQ_5)
        self.ITR_EQ_6: range = range(self.EQ_6)
        self.ITR_EQ_7: range = range(self.EQ_7)
        self.ITR_EQ_8: range = range(self.EQ_8)

        # SYSTEM VARIABLE
        self.GENERATE_LEVELS_FILES: bool = True
        self.COUNTER_ITERATION: int = count
        self.BASE_DIR: Path = Path(__file__).parent.parent
        self.INCLUDE_DIR: Path = self.BASE_DIR / "src_c"

        # NAMES FILES -> ('ADD, SUB', 'MUL, DIV', 'ALL')
        self.HEADER: str = os.path.join(self.INCLUDE_DIR, 'levels.h')
        self.MAIN: str = os.path.join(self.INCLUDE_DIR, 'main.c')
        self.PYX: str = os.path.join(self.INCLUDE_DIR, 'equation_levels.pyx')
        self.SETUP: str = os.path.join(self.BASE_DIR, 'setup_levels.py')
        self.ADD_SUB_BR: str = os.path.join(self.INCLUDE_DIR, 'eq_add_sub_br.c')
        self.MUL_DIV_BR: str = os.path.join(self.INCLUDE_DIR, 'eq_mul_div_br.c')
        self.ADD_SUB_MUL_DIV_BR: str = os.path.join(self.INCLUDE_DIR, 'eq_add_sub_mul_div_br.c')

        # NAMES FILES -> ('EQ_4', 'EQ_5', 'EQ_6', 'EQ_7', 'EQ_8')
        self.HEADER_EQ: str = os.path.join(self.INCLUDE_DIR, 'levels_eq.h')
        self.MAIN_EQ: str = os.path.join(self.INCLUDE_DIR, 'main_eq.c')
        self.PYX_EQ: str = os.path.join(self.INCLUDE_DIR, 'equation_levels.pyx')
        self.SETUP_EQ: str = os.path.join(self.BASE_DIR, 'setup_levels.py')
        self.INCLUDE_EQ_4: str = os.path.join(self.INCLUDE_DIR, 'eq_4.c')
        self.INCLUDE_EQ_5: str = os.path.join(self.INCLUDE_DIR, 'eq_5.c')
        self.INCLUDE_EQ_6: str = os.path.join(self.INCLUDE_DIR, 'eq_6.c')
        self.INCLUDE_EQ_7: str = os.path.join(self.INCLUDE_DIR, 'eq_7.c')
        self.INCLUDE_EQ_8: str = os.path.join(self.INCLUDE_DIR, 'eq_8.c')

        self.OPERATORS: Mapping[str, Callable[[float, float], float]] = MappingProxyType({
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv,
            '^': operator.pow
        })


"""
+----------------------+
//---- 15.09.2025 ----//
|====== Eval_fast =====|
+----------------------+
"""
class EvalEquation(BaseArrays):
    __slots__ = (
        'config',
        'min_len',
        'counter_iteration_max',
        'set_digit',
        'parser',
        'logger'
    )


    def __init__(self, config: EquationConfig) -> None:
        super().__init__()
        self.config: EquationConfig = config
        self.min_len: int = 3
        self.counter_iteration_max: int = 1000
        self.set_digit: set[str] = {str(digit) for digit in range(5001)}
        self.parser = equation_ast.EquationParser()
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(level=logging.INFO)


    def __del__(self) -> None:
        gc.collect()


    def _logging_process_eq(self, marker=True) -> None:
        if marker: self.logger.debug("MAX ITERATION")
        else: self.logger.info("CYCLE ENDED")


    def _toggle_variable_generate_levels_files(self):
        self.config.GENERATE_LEVELS_FILES = False


    def _create_header(self) -> None:
        if self.config.GENERATE_LEVELS_FILES:
            with open(self.config.HEADER, "w") as file:
                file.write(
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


    def _create_header_eq(self) -> None:
        if self.config.GENERATE_LEVELS_FILES:
            with open(self.config.HEADER_EQ, "w") as file:
                file.write(
                    '#ifndef LEVELS_H\n'
                    '#define LEVELS_H\n\n'
                    f'void init{self.config.EQ_N_LW_4}();\n'
                    f'void init{self.config.EQ_N_LW_5}();\n'
                    f'void init{self.config.EQ_N_LW_6}();\n'
                    f'void init{self.config.EQ_N_LW_7}();\n'
                    f'void init{self.config.EQ_N_LW_8}();\n\n'
                    'struct EQ_4 {\n'
                    f'\tunsigned int digit[{self.config.EQ_4}];\n'
                    f'\tchar equation[{self.config.EQ_4}][10000];\n'
                    '};\n'
                    'struct EQ_5 {\n'
                    f'\tunsigned int digit[{self.config.EQ_5}];\n'
                    f'\tchar equation[{self.config.EQ_5}][10000];\n'
                    '};\n'
                    'struct EQ_6 {\n'
                    f'\tunsigned int digit[{self.config.EQ_6}];\n'
                    f'\tchar equation[{self.config.EQ_6}][10000];\n'
                    '};\n'
                    'struct EQ_7 {\n'
                    f'\tunsigned int digit[{self.config.EQ_7}];\n'
                    f'\tchar equation[{self.config.EQ_7}][100000];\n'
                    '};\n'
                    'struct EQ_8 {\n'
                    f'\tunsigned int digit[{self.config.EQ_8}];\n'
                    f'\tchar equation[{self.config.EQ_8}][100000];\n'
                    '};\n\n'
                    'extern struct EQ_4 eq_4;\n'
                    'extern struct EQ_5 eq_5;\n'
                    'extern struct EQ_6 eq_6;\n'
                    'extern struct EQ_7 eq_7;\n'
                    'extern struct EQ_8 eq_8;\n'
                    '#endif'
                )


    def _create_main(self) -> None:
        if self.config.GENERATE_LEVELS_FILES:
            with open(self.config.MAIN, "w") as file:
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


    def _create_main_eq(self) -> None:
        if self.config.GENERATE_LEVELS_FILES:
            with open(self.config.MAIN, "w") as file:
                file.write(
                    '#include <stdio.h>\n'
                    '#include <string.h>\n'
                    '#include "levels_eq.h"\n\n'
                    'extern struct EQ_4 eq_4;\n'
                    'extern struct EQ_5 eq_5;\n'
                    'extern struct EQ_6 eq_6;\n'
                    'extern struct EQ_7 eq_7;\n'
                    'extern struct EQ_8 eq_8;\n\n'
                    'unsigned int maxLengthFour(struct EQ_4* obj, unsigned int numberItr);\n'
                    'unsigned int maxLengthFive(struct EQ_5* obj, unsigned int numberItr);\n'
                    'unsigned int maxLengthSix(struct EQ_6* obj, unsigned int numberItr);\n'
                    'unsigned int maxLengthSeven(struct EQ_7* obj, unsigned int numberItr);\n'
                    'unsigned int maxLengthEight(struct EQ_8* obj, unsigned int numberItr);\n\n'
                    'int main() {\n'
                    '\t	//Length Max\n\n'
                    f'\tinit{self.config.EQ_N_LW_4}();\n'
                    f'\tinit{self.config.EQ_N_LW_5}();\n'
                    f'\tinit{self.config.EQ_N_LW_6}();\n'
                    f'\tinit{self.config.EQ_N_LW_7}();\n'
                    f'\tinit{self.config.EQ_N_LW_8}();\n\n'
                    '\tunsigned int length_eq_4;\n'
                    '\tunsigned int length_eq_5;\n'
                    '\tunsigned int length_eq_6;\n'
                    '\tunsigned int length_eq_7;\n'
                    '\tunsigned int length_eq_8;\n\n'
                    f'\tlength_eq_4 = maxLengthFour(&eq_4, {self.config.EQ_4});\n'
                    f'\tlength_eq_5 = maxLengthFive(&eq_5, {self.config.EQ_5});\n'
                    f'\tlength_eq_6 = maxLengthSix(&eq_6, {self.config.EQ_6});\n'
                    f'\tlength_eq_7 = maxLengthSeven(&eq_7, {self.config.EQ_7});\n'
                    f'\tlength_eq_8 = maxLengthEight(&eq_8, {self.config.EQ_8});\n\n'
                    f'\tfloat memory_eq_4 = (length_eq_4 * {self.config.EQ_4}) / 1000.0f;\n'
                    f'\tfloat memory_eq_5 = (length_eq_5 * {self.config.EQ_5}) / 1000.0f;\n'
                    f'\tfloat memory_eq_6 = (length_eq_6 * {self.config.EQ_6}) / 1000.0f;\n'
                    f'\tfloat memory_eq_7 = (length_eq_7 * {self.config.EQ_7}) / 1000.0f;\n'
                    f'\tfloat memory_eq_8 = (length_eq_8 * {self.config.EQ_8}) / 1000.0f;\n'
                    '\tfloat memoryTotal = memory_eq_4 + memory_eq_5 + memory_eq_6 + memory_eq_7 + memory_eq_8;\n\n'
                    '\tprintf("#==================Start===================================#\\n");\n'
                    '\tprintf("Max length Eq_4: %d\\n", length_eq_4);\n'
                    '\tprintf("Max length Eq_5: %d\\n", length_eq_5);\n'
                    '\tprintf("Max length Eq_6: %d\\n", length_eq_6);\n'
                    '\tprintf("Max length Eq_7: %d\\n", length_eq_7);\n'
                    '\tprintf("Max length Eq_8: %d\\n", length_eq_8);\n'
                    '\tprintf("#==================End=====================================#\\n");\n\n'
                    '\tFILE* file = fopen("result_length.txt", "w");\n\n'
                    '\tif (file == NULL) {\n'
                    '\t\tprintf("File not opened!\\n");\n'
                    '\t\treturn 1;\n'
                    '\t}\n\n'
                    '\tfprintf(file, "result length: \\n");\n'
                    '\tfprintf(file, "Max length Eq_4: %d\\n", length_eq_4);\n'
                    '\tfprintf(file, "Max length Eq_5: %d\\n", length_eq_5);\n'
                    '\tfprintf(file, "Max length Eq_6: %d\\n", length_eq_6);\n'
                    '\tfprintf(file, "Max length Eq_7: %d\\n", length_eq_7);\n'
                    '\tfprintf(file, "Max length Eq_8: %d\\n", length_eq_8);\n'
                    '\tfprintf(file, "\\n");\n'
                    '\tfprintf(file, "Memory Eq_4(kbite): %.1f\\n", memory_eq_4);\n'
                    '\tfprintf(file, "Memory Eq_5(kbite): %.1f\\n", memory_eq_5);\n'
                    '\tfprintf(file, "Memory Eq_6(kbite): %.1f\\n", memory_eq_6);\n'
                    '\tfprintf(file, "Memory Eq_7(kbite): %.1f\\n", memory_eq_7);\n'
                    '\tfprintf(file, "Memory Eq_8(kbite): %.1f\\n", memory_eq_8);\n'
                    '\tfprintf(file, "Memory total(kbite): %.1f\\n", memoryTotal);\n'
                    '\tfclose(file);\n\n'
                    '\treturn 0;\n'
                    '}\n\n'
                    'unsigned int maxLengthFour(struct EQ_4* obj, unsigned int numberItr) {\n'
                    '\tint lengthEq = 0;\n'
                    '\tfor (int i = 0; i < numberItr; i++) {\n'
                    '\t\tif (strlen(obj->equation[i]) > lengthEq)\n'
                    '\t\t\tlengthEq = strlen(obj->equation[i]);\n'
                    '\t}\n'
                    '\treturn lengthEq;\n'
                    '}\n\n'
                    'unsigned int maxLengthFive(struct EQ_5* obj, unsigned int numberItr) {\n'
                    '\tint lengthEq = 0;\n'
                    '\tfor (int i = 0; i < numberItr; i++) {\n'
                    '\t\tif (strlen(obj->equation[i]) > lengthEq)\n'
                    '\t\t\tlengthEq = strlen(obj->equation[i]);\n'
                    '\t}\n'
                    '\treturn lengthEq;\n'
                    '}\n\n'
                    'unsigned int maxLengthSix(struct EQ_6* obj, unsigned int numberItr) {\n'
                    '\tint lengthEq = 0;\n'
                    '\tfor (int i = 0; i < numberItr; i++) {\n'
                    '\t\tif (strlen(obj->equation[i]) > lengthEq)\n'
                    '\t\t\tlengthEq = strlen(obj->equation[i]);\n'
                    '\t}\n'
                    '\treturn lengthEq;\n'
                    '}\n\n'
                    'unsigned int maxLengthSeven(struct EQ_7* obj, unsigned int numberItr) {\n'
                    '\tint lengthEq = 0;\n'
                    '\tfor (int i = 0; i < numberItr; i++) {\n'
                    '\t\tif (strlen(obj->equation[i]) > lengthEq)\n'
                    '\t\t\tlengthEq = strlen(obj->equation[i]);\n'
                    '\t}\n'
                    '\treturn lengthEq;\n'
                    '}\n\n'
                    'unsigned int maxLengthEight(struct EQ_8* obj, unsigned int numberItr) {\n'
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
            with open(self.config.PYX, "w") as file:
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


    def _create_pyx_eq(self) -> None:
        if self.config.GENERATE_LEVELS_FILES:
            with open(self.config.PYX, "w") as file:
                file.write(
                    "cdef set SYMBOL_IF = {\n"
                    "\t'*', '/', '+', '-', '(', ')', '=',\n"
                    "\t'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'\n"
                    '}\n\n'
                    'cdef extern from "levels_eq.h":\n'
                    '\tcdef struct EQ_4:\n'
                    f'\t\tunsigned int digit[{self.config.EQ_4}]\n'
                    f'\t\tchar equation[{self.config.EQ_4}][1000]\n'
                    '\tcdef struct EQ_5:\n'
                    f'\t\tunsigned int digit[{self.config.EQ_5}]\n'
                    f'\t\tchar equation[{self.config.EQ_5}][1000]\n'
                    '\tcdef struct EQ_6:\n'
                    f'\t\tunsigned int digit[{self.config.EQ_6}]\n'
                    f'\t\tchar equation[{self.config.EQ_6}][1000]\n'
                    '\tcdef struct EQ_7:\n'
                    f'\t\tunsigned int digit[{self.config.EQ_7}]\n'
                    f'\t\tchar equation[{self.config.EQ_7}][1000]\n'
                    '\tcdef struct EQ_8:\n'
                    f'\t\tunsigned int digit[{self.config.EQ_8}]\n'
                    f'\t\tchar equation[{self.config.EQ_8}][1000]\n\n'
                    f'\tcdef void init{self.config.EQ_N_LW_4}()\n'
                    f'\tcdef void init{self.config.EQ_N_LW_5}()\n'
                    f'\tcdef void init{self.config.EQ_N_LW_6}()\n'
                    f'\tcdef void init{self.config.EQ_N_LW_7}()\n'
                    f'\tcdef void init{self.config.EQ_N_LW_8}()\n\n'
                    '\tcdef EQ_4 eq_4\n'
                    '\tcdef EQ_5 eq_5\n'
                    '\tcdef EQ_6 eq_6\n'
                    '\tcdef EQ_7 eq_7\n'
                    '\tcdef EQ_8 eq_8\n\n\n'
                    'def init():\n'
                    f'\tinit{self.config.EQ_N_LW_4}()\n'
                    f'\tinit{self.config.EQ_N_LW_5}()\n'
                    f'\tinit{self.config.EQ_N_LW_6}()\n'
                    f'\tinit{self.config.EQ_N_LW_7}()\n'
                    f'\tinit{self.config.EQ_N_LW_8}()\n\n\n'
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
                    'def get_digit_4(unsigned int index):\n'
                    '\treturn eq_4.digit[index]\n\n\n'
                    'cpdef get_equations_4(unsigned int index):\n'
                    "\tcdef str eqs = bytes(eq_4.equation[index]).decode('utf-8')\n"
                    '\treturn list_eq(eqs)\n\n\n'
                    'def get_digit_5(unsigned int index):\n'
                    '\treturn eq_5.digit[index]\n\n\n'
                    'cpdef get_equations_5(unsigned int index):\n'
                    "\tcdef str eqs = bytes(eq_5.equation[index]).decode('utf-8')\n"
                    '\treturn list_eq(eqs)\n\n\n'
                    'def get_digit_6(unsigned int index):\n'
                    '\treturn eq_6.digit[index]\n\n\n'
                    'cpdef get_equations_6(unsigned int index):\n'
                    "\tcdef str eqs = bytes(eq_6.equation[index]).decode('utf-8')\n"
                    '\treturn list_eq(eqs)\n\n\n'
                    'def get_digit_7(unsigned int index):\n'
                    '\treturn eq_7.digit[index]\n\n\n'
                    'cpdef get_equations_7(unsigned int index):\n'
                    "\tcdef str eqs = bytes(eq_7.equation[index]).decode('utf-8')\n"
                    '\treturn list_eq(eqs)\n\n\n'
                    'def get_digit_8(unsigned int index):\n'
                    '\treturn eq_8.digit[index]\n\n\n'
                    'cpdef get_equations_8(unsigned int index):\n'
                    "\tcdef str eqs = bytes(eq_8.equation[index]).decode('utf-8')\n"
                    '\treturn list_eq(eqs)\n'
                )


    def _create_setup(self)-> None:
        if self.config.GENERATE_LEVELS_FILES:
            with open(self.config.SETUP, "w") as file:
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


    def _create_setup_eq(self) -> None:
        if self.config.GENERATE_LEVELS_FILES:
            with open(self.config.SETUP, "w") as file:
                file.write(
                    'from setuptools import setup, Extension\n'
                    'from Cython.Build import cythonize\n\n'
                    'extension = [\n'
                    '\tExtension(\n'
                    "\t\t'equation_levels',\n"
                    '\t\tsources=[\n'
                    "\t\t\t'src_c/equation_levels.pyx',\n"
                    "\t\t\t'src_c/eq_4.c',\n"
                    "\t\t\t'src_c/eq_5.c',\n"
                    "\t\t\t'src_c/eq_6.c',\n"
                    "\t\t\t'src_c/eq_7.c',\n"
                    "\t\t\t'src_c/eq_8.c'\n"
                    '\t\t],\n'
                    "\t\tinclude_dirs=['.']\n"
                    '\t)\n'
                    ']\n\n'
                    "setup(name='equation_levels', ext_modules=cythonize(extension, language_level='3'))"
                )


    def _create_add_sub_bracket(self) -> None:
        with open(self.config.ADD_SUB_BR, "w") as file:
            file.write("#include \"levels.h\"\n")
            file.write("#include <string.h>")
            file.write("\n\n")
            file.write("struct EqAddSubBracket AddSubBracket;\n")
            file.write("\n")


    def _create_mul_div_bracket(self) -> None:
        with open(self.config.MUL_DIV_BR, "w") as file:
            file.write("#include \"levels.h\"\n")
            file.write("#include <string.h>")
            file.write("\n\n")
            file.write("struct EqMulDivBracket MulDivBracket;\n")
            file.write("\n")


    def _create_add_sub_mul_div_bracket(self) -> None:
        with open(self.config.ADD_SUB_MUL_DIV_BR, "w") as file:
            file.write("#include \"levels.h\"\n")
            file.write("#include <string.h>")
            file.write("\n\n")
            file.write("struct EqAddSubMulDivBracket AddSubMulDivBracket;\n")
            file.write("\n")


    def _create_eq_4(self) -> None:
        with open(self.config.INCLUDE_EQ_4, "w") as file:
            file.write("#include \"levels_eq.h\"\n")
            file.write("#include <string.h>")
            file.write("\n\n")
            file.write("struct EQ_4 eq_4;\n")
            file.write("\n")


    def _create_eq_5(self) -> None:
        with open(self.config.INCLUDE_EQ_5, "w") as file:
            file.write("#include \"levels_eq.h\"\n")
            file.write("#include <string.h>")
            file.write("\n\n")
            file.write("struct EQ_5 eq_5;\n")
            file.write("\n")


    def _create_eq_6(self) -> None:
        with open(self.config.INCLUDE_EQ_6, "w") as file:
            file.write("#include \"levels_eq.h\"\n")
            file.write("#include <string.h>")
            file.write("\n\n")
            file.write("struct EQ_6 eq_6;\n")
            file.write("\n")


    def _create_eq_7(self) -> None:
        with open(self.config.INCLUDE_EQ_7, "w") as file:
            file.write("#include \"levels_eq.h\"\n")
            file.write("#include <string.h>")
            file.write("\n\n")
            file.write("struct EQ_7 eq_7;\n")
            file.write("\n")


    def _create_eq_8(self) -> None:
        with open(self.config.INCLUDE_EQ_8, "w") as file:
            file.write("#include \"levels_eq.h\"\n")
            file.write("#include <string.h>")
            file.write("\n\n")
            file.write("struct EQ_8 eq_8;\n")
            file.write("\n")


    def _itr_varint(self, number_len: int) -> range:
        match number_len:
            case 4: return self.config.ITR_EQ_4
            case 5: return self.config.ITR_EQ_5
            case 6: return self.config.ITR_EQ_6
            case 7: return self.config.ITR_EQ_7
            case 8: return self.config.ITR_EQ_8
            case _: return self.config.ITR_EQ_8


    def _file_name_variant(self, number_len: int) -> str:
        match number_len:
            case 4: return self.config.INCLUDE_EQ_4
            case 5: return self.config.INCLUDE_EQ_5
            case 6: return self.config.INCLUDE_EQ_6
            case 7: return self.config.INCLUDE_EQ_7
            case 8: return self.config.INCLUDE_EQ_8
            case _: return self.config.INCLUDE_EQ_8


    def _int_variant(self, number_len) -> int:
        match number_len:
            case 4: return self.config.EQ_4
            case 5: return self.config.EQ_5
            case 6: return self.config.EQ_6
            case 7: return self.config.EQ_7
            case 8: return self.config.EQ_8
            case _: return self.config.EQ_8


    def _name_struct_variant(self, number_len: int) -> str:
        match number_len:
            case 4: return self.config.EQ_N_LW_4
            case 5: return self.config.EQ_N_LW_5
            case 6: return self.config.EQ_N_LW_6
            case 7: return self.config.EQ_N_LW_7
            case 8: return self.config.EQ_N_LW_8
            case _: return self.config.EQ_N_LW_8


    def _create_file_variant(self, number_len: int) -> None:
        match number_len:
            case 4: self._create_eq_4()
            case 5: self._create_eq_5()
            case 6: self._create_eq_6()
            case 7: self._create_eq_7()
            case 8: self._create_eq_8()
            case _: self._create_eq_8()


    @staticmethod
    def _file_init(
            i_itr: int,
            res_eq: tuple[str, set[str]],
            f_name: str, str_name: str,
            op_counter: int
    ) -> None:
        res_str: str = '\n\t'
        len_str: int = len(res_eq[1])

        for j, eq in  enumerate(res_eq[1]):
            if j == 0:
                res_str += '\"' + eq + ', '
            elif j != len_str - 1 and j % 2 == 0:
                res_str += '\"' + eq + ', '
            elif j != len_str - 1:
                res_str += eq + ',\"\n\t'
            elif j == len_str - 1 and len_str % 2 != 0:
                res_str += '\"' + eq
            else:
                res_str += eq
        res_str += '\"'

        with open(f_name, "a") as file:
            if i_itr == 0:
                file.write(f"void init{str_name}() {{\n")

            file.write(f"\t{str_name}.digit[{i_itr}] = {int(res_eq[0])};\n")
            file.write(f'\tstrcpy({str_name}.equation[{i_itr}], {res_str});\n')

            if i_itr == op_counter - 1:
                file.write("}")
            if i_itr != op_counter - 1:
                file.write("\n")


    def is_valid_equation(self, equation: str) -> bool:
        left: str
        right: str
        left_value: float
        right_value: float

        left, right = equation.split('=')
        left_value = self.parser.eval_fast_cpp(left)
        right_value = self.parser.eval_fast_cpp(right)
        return (left_value and right_value) is not None and left_value == right_value


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
        if self.parser.is_valid_equation_cpp(expr_result):
            return expr_result
        return ""


    def process_equation_one(self, digit: str) -> str | None:
        number_len: int = len(digit)
        counter: int = 0
        expr: str
        eq_pos: int
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

        expr: str
        eq_pos: int
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
            expr: str
            eq_pos: int
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
            expr: str
            eq_pos: int
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


    def equation_export_c(self, number_len: int) -> None:
        res_tup: tuple[str, set[str]]
        set_unique: set[str] = set()

        # VARIABLES -> EXPORT C
        int_variant: int = self._int_variant(number_len)
        itr_variant: range = self._itr_varint(number_len)
        struct_variant: str = self._name_struct_variant(number_len)
        file_name_variant: str = self._file_name_variant(number_len)

        # CREATE FILES -> EXPORT C
        self._create_header_eq()
        self._create_main_eq()
        self._create_pyx_eq()
        self._create_setup_eq()
        self._toggle_variable_generate_levels_files()
        self._create_file_variant(number_len)


        def process_eq() -> tuple[str, set[str]]:
            nonlocal number_len

            counter: int = 0
            digit: str = ''
            expr: str
            eq_pos: int
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


        for i in itr_variant:
            while True:
                res_tup = process_eq()
                if len(res_tup[1]) >= self.min_len and res_tup[0] not in set_unique:
                    set_unique.add(res_tup[0])
                    break
            self._file_init(i, res_tup, file_name_variant, struct_variant, int_variant)
        self._logging_process_eq(False)


if __name__ == "__main__":
    object_config = EquationConfig(500200)
    ev = EvalEquation(object_config)
    # print(ev.process_equation_one('1234'))
    # print(ev.process_equation_one('12345'))
    # print(ev.process_equation_one('123456'))
    # print(ev.process_equation_one('1234567'))
    # print(ev.process_equation_one('12345678'))
    print(ev.process_equation_all_possible('1234'))
    print(ev.process_equation_all_possible('12345'))
    print(ev.process_equation_all_possible('123456'))
    print(ev.process_equation_all_possible('1234567'))
    print(ev.process_equation_all_possible('12345678'))
    # ev.equation_add_sub_bracket(4)
    # ev.equation_add_sub_bracket(4, False)
    # ev.equation_add_sub_mul_div_bracket(4)
    # ev.equation_export_c(4)
    # ev.equation_export_c(5)
    # ev.equation_export_c(6)
    # ev.equation_export_c(7)
    # ev.equation_export_c(8)
