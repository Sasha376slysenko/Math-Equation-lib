import timeit

from math_equations import equation_lib
from math_equation_lib.math_equations.eq import EvalEquation as EvalEval
from math_equation_lib.math_equations.eq import EquationConfig as EquationConfig

from sympy import sympify
from numexpr import evaluate
from dict_in_for import *
from colorama import *
from matplotlib import pyplot as plt

obj_evl = EquationConfig(15200)
eval_eval = EvalEval(obj_evl)

obj_custom = equation_lib.EquationConfig(15200)
custom_eval = equation_lib.EvalEquation(obj_custom)

times_custom: list[list[float]] = []
times_python: list[list[float]] = []
times_sympy: list[list[float]] = []
times_numexpr: list[list[float]] = []
times_custom_4: list[list[float]] = []
times_python_4: list[list[float]] = []

for key in dict_equations.keys():
    time_custom: list[float] = []
    time_python: list[float] = []
    time_sympy: list[float] = []
    time_numexpr: list[float] = []
    for el in dict_equations[key]:
        time_custom.append(timeit.timeit(
            "custom_eval.is_valid_equation(el)",
            globals={"custom_eval": custom_eval, "el": el},
            number=1_000) / 1_000
        )
        time_python.append(timeit.timeit(
            "eval_eval.is_valid_equation(el)",
            globals={"eval_eval": eval_eval, "el": el},
            number=1_000) / 1_000
        )
        time_sympy.append(timeit.timeit(
            "sympify(el)",
            globals={"sympify": sympify, "el": el.replace('=', '==')},
            number=1_000 ) / 1_000
        )
        time_numexpr.append(timeit.timeit(
            "evaluate(el)",
            globals={"evaluate": evaluate, "el": el.replace('=', '==')},
            number=1_000 ) / 1_000
        )
    times_custom.append(time_custom)
    times_python.append(time_python)
    times_sympy.append(time_sympy)
    times_numexpr.append(time_numexpr)
print(Back.LIGHTGREEN_EX + Fore.BLACK + 'PROCESS CHECK ONE EQUATION FINISHED!', end="")
print(Style.RESET_ALL)

for key in dict_digits.keys():
    time_custom_4: list[float] = []
    time_python_4: list[float] = []
    for i, el in enumerate(dict_digits[key]):
        print(Back.LIGHTCYAN_EX + Fore.BLACK + f"counter digit: {i+1}, KEY: {key}", end="")
        print(Style.RESET_ALL)

        time_custom_4.append(timeit.timeit(
            "custom_eval.process_equation_all_possible(el)",
            globals={"custom_eval": custom_eval, "el": el},
            number=45) / 45
        )
        time_python_4.append(timeit.timeit(
            "eval_eval.process_equation_all_possible(el)",
            globals={"eval_eval": eval_eval, "el": el},
            number=45) / 45
        )
    times_custom_4.append(time_custom_4)
    times_python_4.append(time_python_4)
print(Back.LIGHTGREEN_EX + Fore.BLACK + 'PROCESS GENERATION EQUATION FINISHED!', end="")
print(Style.RESET_ALL)


def plot_save(dict_test, times_test, times_custom_test, label: str):
    all_times_test:list[float] = []
    all_times_custom_test:list[float] = []
    list_key_test: list[str] = dict_test.keys()

    for key_i, time_custom_i, time_test_i in zip(list_key_test, times_custom_test, times_test):
        plt.figure(figsize=(19, 5))
        plt.yscale('log')
        plt.title('Порівняння часу виконання', fontsize=16)
        plt.xlabel('Рівності', fontsize=12)
        plt.ylabel('Час (сек)', fontsize=12)
        plt.plot(dict_test[key_i], time_custom_i, color="green", marker="^", linewidth=3, label="custom_eval")
        plt.plot(dict_test[key_i], time_test_i, color="red", marker="o", linewidth=3, label=label, linestyle="--")
        plt.legend(loc="best")
        plt.savefig(f"test/res_time_speed/figure_{key_i}.{label}.png", dpi=200)
        plt.close()

        all_times_custom_test.extend(time_custom_i)
        all_times_test.extend(time_test_i)

    plt.figure(figsize=(17, 5))
    plt.grid(axis='y')
    plt.title('Порівняння часу виконання', fontsize="16")
    plt.xlabel('Рівності', fontsize=12)
    plt.ylabel('Час (сек)', fontsize=12)
    plt.boxplot(
        [all_times_test, all_times_custom_test],
        patch_artist=True,
        tick_labels=[label, 'custom eval'],
    )
    plt.savefig(f"test/res_time_speed/figure_boxplot.{label}.boxplot.png", dpi=300)
    plt.close()


if __name__ == '__main__':
    plot_save(dict_equations, times_python, times_custom, 'eval')
    plot_save(dict_equations, times_numexpr, times_custom, 'numexpr')
    plot_save(dict_equations, times_sympy,  times_custom, 'sympy')
    plot_save(dict_digits, times_python_4, times_custom_4, 'eval')
