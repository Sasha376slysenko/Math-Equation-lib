# Math Equation lib

## Короткий опис math equations lib
Math Equations lib - бібліотека для генерації всіх можливих рівностей та перевірки рівностей  з використанням операторів 
**'+', '-', '*', '/', '^', '()'**. Підходить для навчальних задач, тестування алгоритмів, генерації статичних рівностей
для C/pyx. Використовує менше ресурсів процесора, оперативної пам'яті та час виконання порівняно з вбудованою функцією 
'eval' в Python, яка швидко переповнює оперативну пам'ять.

## Структура проєкту
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

## Можливості
- Перевірка рівностей
- Генерація **однієї рівності** з заданого числа (довжиною від 4 до 8 цифр)
- Генерація **всіx можливих рівностей** для такої довжини чисел:
    1. 4
    2. 5
    3. 6
    4. 7
    5. 8
- Генерація та **експорт в static data на C/pyx**:
    1. Всі можливі рівності з операторами '+', '-', '()'
    2. Всі можливі рівності з операторами '*', '/', '()'
    3. Всі можливі рівності з операторами '+', '-', '*', '/', '()'

## Встановлення
```bash
pip install git+https://github.com/username/math-equations-lib.git
```

## Приклад перевірки рівності
```python
from math_equations import equation_lib

# Створюємо конфігурацію з максимальною кількістю комбінації
object_config = equation_lib.EquationConfig(15200)

# Створюємо об'єкт для генерації та перевірки рівностей
object_ev = equation_lib.EvalEquation(object_config)

# Повертає True, якщо рівність правильна. False, якщо рівність неправильна 
print(object_ev.is_valid_equation('(3+4)*1=9-2')) # ->  True
print(object_ev.is_valid_equation('(3+4)*1=9+2')) # ->  False
```

## Приклад використання Генерації однієї рівності
```python
from math_equations import equation_lib

# Створюємо конфігурацію з максимальною кількістю комбінації
object_config = equation_lib.EquationConfig(15200)

# Створюємо об'єкт для генерації та перевірки рівностей
object_ev = equation_lib.EvalEquation(object_config)

# Повертає першу знайдену математичну рівність
print(object_ev.process_equation_one('1234')) # оператори '+', '-', '*', '/', '^', '()'
```

## Приклад використання Генерації всіx можливих рівностей
```python
from math_equations import equation_lib

# Створюємо конфігурацію з максимальною кількістю комбінації
object_config = equation_lib.EquationConfig(15200)

# Створюємо об'єкт для генерації та перевірки рівностей
object_ev = equation_lib.EvalEquation(object_config)

# Повертає всі знайдені рівності в межах заданої максимальної комбінації операторів
print(object_ev.process_equation_all_possible('1234')) # оператори '+', '-', '*', '/', '^', '()'
```

## Приклад використання Генерації та експорт в  static data на C/pyx
```python
from math_equations import equation_lib

# Створюємо конфігурацію з максимальною кількістю комбінації
object_config = equation_lib.EquationConfig(15200)

# Створюємо об'єкт для генерації та перевірки рівностей
object_ev = equation_lib.EvalEquation(object_config)

# Генерує всі можливі рівності для 4-значного числа та зберігає у C-файлах
object_ev.equation_add_sub_bracket(4)         # оператори '+', '-', '()'
object_ev.equation_add_sub_bracket(4, False)  # оператори '*', '/', '()'
object_ev.equation_add_sub_mul_div_bracket(4) # оператори '+', '-', '*', '/', '()'
```