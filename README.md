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
│  ├─eq.py            # Python eval
│  └─equation_lib.py  # Own implementation
├─test/
│  ├─data_cpu/
│  │ ├─custom_eval_generation_eq.csv
│  │ └─python_eval_generation_eq.csv
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

## Principle of operation
1. In order to check whether the equality is correct, you must first pass the input characters through the lexical analyzer.
2. Which will create tokens then build a tree based on mathematical operations.
3. And recursively bypass it with a gradual decrease in the priority of mathematical operations.
4. The tree is circumvented according to the rules of priority of the operation ('()', '^', '*, /', '+, -').
5. Recursive evaluation of tree nodes allows you to get the value of the expression and check whether there is equality
   correct (left part == right part).

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

## The library was tested on Unittest
```bash
python -m unittest discover -s test -p "unittest_*.py"
```

### Unittests cover tests for all mathematical operators
```python
import unittest
from math_equations import equation_lib

class TestEvalEquation(unittest.TestCase):
    def setUp(self)-> None:
        # Create configuration with the maximum number of combinations
        self.object_config = equation_lib.EquationConfig(500)

        # Create an object for generating and verifying equations
        self.eq = equation_lib.EvalEquation(self.object_config)

    def test_eval_fast_one(self)-> None:
        self.assertEqual(self.eq._eval_fast('7+5'), 12)
        self.assertEqual(self.eq._eval_fast('3-3'), 0)
        self.assertEqual(self.eq._eval_fast('2*3'), 6)
        self.assertEqual(self.eq._eval_fast('3/3'), 1)
        self.assertEqual(self.eq._eval_fast('3^3'), 27)

    def test_eval_fast_two(self)-> None:
        self.assertEqual(self.eq._eval_fast('-3+3+7'), 7)
        self.assertEqual(self.eq._eval_fast('-7+8'), 1)
        self.assertEqual(self.eq._eval_fast('-1-7+8'), 0)

    def test_eval_fast_three(self)-> None:
        self.assertEqual(self.eq._eval_fast('1--1'), 2)

    def test_eval_fast_four(self)-> None:
        self.assertEqual(self.eq._eval_fast('(3+4)*1'), 7)
        self.assertEqual(self.eq._eval_fast('(3*4)/2'), 6)
        self.assertEqual(self.eq._eval_fast('(3*4)*2'), 24)

    def test_eval_fast_five(self)-> None:
        self.assertEqual(self.eq._eval_fast('(1+8-9-1+2)+5'), 6)
        self.assertEqual(self.eq._eval_fast('(5*9-6+3)*6'), 252)
        self.assertEqual(self.eq._eval_fast('(-1-7+8)'), 0)
        self.assertEqual(self.eq._eval_fast('(1+2)'), 3)
        self.assertEqual(self.eq._eval_fast('-1+5'), 4)

    def test_eval_fast_six(self) -> None:
        self.assertEqual(self.eq._eval_fast('-1-5'), -6)
        self.assertEqual(self.eq._eval_fast('(-1+2)+5'), 6)
        self.assertEqual(self.eq._eval_fast('(1+2)'), 3)
        self.assertEqual(self.eq._eval_fast('1--1+5'), 7)
        self.assertEqual(self.eq._eval_fast('1-(2-3)+3+5'), 10)
        self.assertEqual(self.eq._eval_fast('1+(3-4)+3'), 3)
        self.assertEqual(self.eq._eval_fast('-3*5'), -15)
        self.assertEqual(self.eq._eval_fast('-7-8'), -15)
        self.assertEqual(self.eq._eval_fast('(5*9-6+3)*6'), 252)
        self.assertEqual(self.eq._eval_fast('6+(1+5)+2+4-9'), 9)
        self.assertEqual(self.eq._eval_fast('8-1^(3/4/2)'), 7)
        self.assertEqual(self.eq._eval_fast('8-1^(3^4^2)'), 7)
        self.assertEqual(self.eq._eval_fast('5+3-(9-8)^6'), 7)
        self.assertEqual(self.eq._eval_fast('5+3-(8-9)^3'), 9)
        self.assertEqual(self.eq._eval_fast('2/3*6'), 4)
        self.assertEqual(self.eq._eval_fast('(9-6)^(9-6)'), 27)
        self.assertEqual(self.eq._eval_fast('(8-9)^(9-6)'), -1)
        self.assertEqual(self.eq._eval_fast('(8-9)^(9-5)'), 1)
        self.assertEqual(self.eq._eval_fast('(9-8)^(6-9)'), 1)
```

## Performance

Below is a comparison of the RAM usage of 'equation_lib' with a naive Python implementation

### RAM usage

![Memory usage small input](test/res_test_ram/test_generation_eq_4-generation-equation-1.png)

- When generating a large number of equalities, '' takes up less RAM.
- The built-in function '' compiles the string into bytecode each time, which increases resource consumption.

![Memory usage medium input](test/res_test_ram/test_generation_eq_4-generation-equation-2.png)

- When calling more than 30 equalities, 'eval' starts to load memory significantly more.

![Memory usage hard input](test/res_test_ram/test_generation_eq_4-generation-equation-3.png)

- There is a sharp jump in memory usage in 'eval'
- This is explained by additional Cpython allocations during bulk calls.

![Memory usage strec input](test/res_test_ram/test_generation_eq_4-generation-equation-4.png)

- After the jump, the memory stabilizes at a new level.
- 'equation_lib' shows more stable results even under high load.