# Math Equation lib

## Description
Math Equations lib - a library for generating all possible equalities and checking equality using the operators
**'+', '-', '*', '/', '^', '()'**. Suitable for educational tasks, algorithm testing, and generating static equations
for C/pyx. It uses less CPU, memory, and execution time compared to Python's built-in eval function, which quickly exhausts memory.

## Project Structure
```text
math_equation_lib/
├─math_equations/
│  ├─__init__.py
│  └─equation_lib.py
├─test/
│  ├─res_test_cpu/
│  │ ├─Енергоспоживання з часом.png
│  │ ├─Завантаження CPU.png
│  │ └─...
│  ├─res_test_ram/
│  │ ├─test_equations_check.png
│  │ ├─test_generation_digits.png
│  │ └─...
│  ├─res_time_speed/
│  │ ├─figure_4.eval.png
│  │ ├─figure_4.numexpr.png
│  │ └─...
│  ├─custom_eval_generation_eq.csv
│  ├─dict_in_for
│  ├─eq.py
│  ├─python_eval_generation_eq.csv
│  ├─test_cpu.py
│  ├─test_ram.py
│  ├─time_speed.py
│  ├─time_test.py
│  └─unittest_equation_lib.py
├─eq_add_sub_br.c
├─eq_mul_div_br.c
├─eq_add_sub_mul_div_br.c
├─levels.h
├─main.c
├─setup_levels.py
├─README_ua.md
└─README.md
```

## Features
- Verify equations
- Generate **a single equation** from a given number (length from 4 to 8 digits)
- Generate **all possible equations** for numbers of the following lengths:
    1. 4
    2. 5
    3. 6
    4. 7
    5. 8
- Generate and **export to static data in C/pyx**:
    1. All possible equations with operators '+', '-', '()'
    2. All possible equations with operators '*', '/', '()'
    3. All possible equations with operators '+', '-', '*', '/', '()'

## Installation
```bash
pip install git+https://github.com/username/math-equations-lib.git
```

## Example: Equation Validation
```python
from math_equations import equation_lib

# Create configuration with the maximum number of combinations
object_config = equation_lib.EquationConfig(15200)

# Create an object for generating and verifying equations
object_ev = equation_lib.EvalEquation(object_config)

# Returns True if the equality is true. False if the equality is not true
print(object_ev.is_valid_equation('(3+4)*1=9-2')) # ->  True
print(object_ev.is_valid_equation('(3+4)*1=9+2')) # ->  False
```

## Example: Generate a Single Equation
```python
from math_equations import equation_lib

# Create configuration with the maximum number of combinations
object_config = equation_lib.EquationConfig(15200)

# Create an object for generating and verifying equations
object_ev = equation_lib.EvalEquation(object_config)

# Returns the first found mathematical equation
print(object_ev.process_equation_one('1234')) # operators '+', '-', '*', '/', '^', '()'
```

## Example: Generate All Possible Equations
```python
from math_equations import equation_lib

# Create configuration with the maximum number of combinations
object_config = equation_lib.EquationConfig(15200)

# Create an object for generating and verifying equations
object_ev = equation_lib.EvalEquation(object_config)

# Returns all found equations within the maximum combination limit
print(object_ev.process_equation_all_possible('1234')) # operators '+', '-', '*', '/', '^', '()'
```

## Example: Generate and Export to Static Data in C/pyx
```python
from math_equations import equation_lib

# Create configuration with the maximum number of combinations
object_config = equation_lib.EquationConfig(15200)

# Create an object for generating and verifying equations
object_ev = equation_lib.EvalEquation(object_config)

# Generate all possible equations for a 4-digit number and save to C files
object_ev.equation_add_sub_bracket(4)         # operators '+', '-', '()'
object_ev.equation_add_sub_bracket(4, False)  # operators '*', '/', '()'
object_ev.equation_add_sub_mul_div_bracket(4) # operators '+', '-', '*', '/', '()'
```