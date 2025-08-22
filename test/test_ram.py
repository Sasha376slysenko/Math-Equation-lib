import gc
import numpy as np
import tracemalloc as trc

from equation_lib import EvalEquation as Custom_eval
from equation_lib import EquationConfig as Custom_config

from eq import EquationConfig as Config_eval
from eq import EvalEquation as Eval_eval

from dict_in_for import *
from typing import Callable
from sympy import sympify
from numexpr import evaluate
from matplotlib import pyplot as plt
from colorama import Back, Fore, Style


object_custom = Custom_config(4000)
custom_eval = Custom_eval(object_custom)

object_eval = Config_eval(4000)
eval_eval = Eval_eval(object_eval)


"""
    +--------------------------------------+
    | Вимірювання використання RAM(bytes): |
    | 1. Sizes equation                    |
    | 2. Counts equation                   |
    | 3. APPEND total_size / total_count   |
    +--------------------------------------+
"""
def benchmark_ram_keys(marker: bool, func: Callable[[str], bool]) -> np.ndarray:
    total_size_eq: float
    total_count_eq: float
    result_array: np.ndarray[np.ndarray[float]] = np.empty((17, 10), dtype=np.float64)

    trc.start(25)
    for i, key in enumerate(dict_equations.keys()):
        for j, eq in enumerate(dict_equations[key]):
            snapshot_1 = trc.take_snapshot()
            if marker:func(eq)
            else: func(eq.replace('=', '=='))
            snapshot_2 = trc.take_snapshot()
            top_stats = snapshot_2.compare_to(snapshot_1, 'lineno')

            # update variables
            total_size_eq = 0
            total_count_eq = 0

            for stat in top_stats:
                if stat.traceback[0].filename != "D:\python310\lib\\tracemalloc.py":
                    if stat.traceback[0].filename != "P:\Python_work\Python_work\HARD_WORK_PY\Game\Гра\GameWeb_finish_4\\test\\test_cpu_1.py":
                        total_size_eq += stat.size
                        total_count_eq += stat.count

            if total_count_eq == 0: result_array[i, j] = 0.0
            else: result_array[i, j] = total_size_eq / total_count_eq /  1024
    trc.stop()
    gc.collect()
    return result_array


"""
    +----------------------------------------------------+
    | Вимірювання використання RAM(bytes) generation eq: |
    | 1. Sizes equation                                  |
    | 2. Counts equation                                 |
    | 3. APPEND total_size / total_count                 |
    +----------------------------------------------------+
"""
def benchmark_process_src(func: Callable[[str], bool]) -> np.ndarray:
    print(Back.LIGHTGREEN_EX + Fore.BLACK + "START GENERATION EQ", end="")
    print(Style.RESET_ALL)
    total_size_eq: float
    total_count_eq: float
    result_array: np.ndarray[np.ndarray[float]] = np.empty((5, 30), dtype=np.float64)

    trc.start(25)
    for i, key in enumerate(dict_digits.keys()):
        for j, digit in enumerate(dict_digits[key]):
            print(Back.LIGHTCYAN_EX + Fore.BLACK + f"counter digit: {j+1}, KEY: {key}", end="")
            print(Style.RESET_ALL)

            snapshot_1 = trc.take_snapshot()
            func(digit)
            snapshot_2 = trc.take_snapshot()
            top_stats = snapshot_2.compare_to(snapshot_1, 'lineno')

            # update variables
            total_size_eq = 0
            total_count_eq = 0

            for stat in top_stats:
                if stat.traceback[0].filename != "D:\python310\lib\\tracemalloc.py":
                    if stat.traceback[0].filename != "P:\Python_work\Python_work\HARD_WORK_PY\Game\Гра\GameWeb_finish_4\\test\\test_cpu_1.py":
                        total_size_eq += stat.size
                        total_count_eq += stat.count

            if total_count_eq == 0: result_array[i, j] = 0.0
            else: result_array[i, j] = total_size_eq / total_count_eq / 1024
    trc.stop()
    gc.collect()
    print(Back.LIGHTGREEN_EX + Fore.BLACK + "ENDED GENERATION EQ", end="")
    print(Style.RESET_ALL)
    return result_array


"""
    +--------------------------------------+
    | Побудова графіків використання RAM:  |
    | 1. Custom eval                       |
    | 2. Eval python                       |
    | 3. Sympy                             |
    | 4. Numexpr                           |
    +--------------------------------------+
"""
def graph_size(res_1_itr: np.ndarray, res_2_itr: np.ndarray, res_3_itr: np.ndarray, res_4_itr: np.ndarray) -> None:
    labels: list[str] = ['custom_eval', 'eval', 'sympy', 'numexpr']


    def plot_graph(res_1: np.ndarray, res_2: np.ndarray, i: int, name_file) -> None:
        nonlocal labels

        plt.figure(figsize=(18, 6))
        plt.title('Використання оперативної пам\'яті', fontsize=16)
        plt.ylabel('пам\'ять(kb)', fontsize=14)
        plt.xlabel('Рівності', fontsize=14)
        plt.plot(dict_equations[key], res_1, 'g-', marker="o", label=labels[0])
        plt.plot(dict_equations[key], res_2, 'r--', marker="^", label=labels[i])
        plt.legend(loc='best')
        plt.savefig(f"res_test_ram/test_{name_file}_eq_{key}.png", dpi=300)
        plt.close()


    for m_res_1, m_res_2, m_res_3, m_res_4, key in zip(res_1_itr, res_2_itr, res_3_itr, res_4_itr, dict_equations.keys()):
        plot_graph(m_res_1, m_res_2, 1, 'ptn')
        plot_graph(m_res_1, m_res_3, 2, 'smp')
        plot_graph(m_res_1, m_res_4, 3, 'nxp')

    # boxplot ('custom eval', 'eval', 'sympy', 'numexpr')
    plt.figure(figsize=(18, 9))
    plt.title('Використання оперативної пам\'яті (custom eval, eval, sympy, numexpr)', fontsize=16)
    plt.ylabel('пам\'ять(kb)', fontsize=14)
    plt.boxplot(
        [np.ravel(res_1_itr), np.ravel(res_2_itr), np.ravel(res_3_itr), np.ravel(res_4_itr)],
        patch_artist=True,
        tick_labels=['custom eval', 'eval', 'sympy', 'numexpr']
    )
    plt.savefig(f"res_test_ram/test_equations_check.png", dpi=300)
    plt.close()


"""
    +--------------------------------------+
    | Побудова графіків використання RAM:  |
    | 1. Custom eval                       |
    | 2. Eval python                       |
    +--------------------------------------+
"""
def graph_process_src(res_generation_1: np.ndarray, res_generation_2: np.ndarray) -> None:
    for res_1, res_2,  key in zip(res_generation_1, res_generation_2, dict_digits.keys()):
        plt.figure(figsize=(18, 6))
        plt.title('Використання оперативної пам\'яті', fontsize=16)
        plt.ylabel('пам\'ять(kb)', fontsize=14)
        plt.xlabel('Числа', fontsize=14)
        plt.plot(dict_digits[key], res_1, 'g-', marker="o", label='custom eval')
        plt.plot(dict_digits[key], res_2, 'r--', marker="^", label='eval')
        plt.legend(loc='best')
        plt.savefig(f"res_test_ram/test_generation_eq_{key}.png", dpi=300)
        plt.close()

    # boxplot ('custom eval', 'eval)
    plt.figure(figsize=(18, 9))
    plt.title('Використання оперативної пам\'яті (custom eval, eval, sympy, numexpr)', fontsize=16)
    plt.ylabel('пам\'ять(kb)', fontsize=14)
    plt.boxplot(
        [np.ravel(res_generation_1), np.ravel(res_generation_2)],
        patch_artist=True,
        tick_labels=['custom eval', 'eval']
    )
    plt.savefig(f"res_test_ram/test_generation_digits.png", dpi=300)
    plt.close()


if __name__ == '__main__':
    res_ctm = benchmark_ram_keys(True, custom_eval.is_valid_equation)
    res_ptn = benchmark_ram_keys(True, eval_eval.is_valid_equation)
    res_smp = benchmark_ram_keys(False, sympify)
    res_nxp = benchmark_ram_keys(False,evaluate)
    graph_size(res_ctm, res_ptn, res_smp, res_nxp)

    res_generation_eqs_cst = benchmark_process_src(custom_eval.process_equation_all_possible)
    res_generation_eqs_ptn = benchmark_process_src(eval_eval.process_equation_all_possible)
    graph_process_src(res_generation_eqs_cst, res_generation_eqs_ptn)