import equation_levels
import time
from colorama import Back, Fore, Style

equation_levels.init()


def time_calculate(end_process, start_porcess):
    print(Back.LIGHTGREEN_EX + Fore.BLACK + f"time(ms): {(end_process - start_porcess) * 10**3}", end="")
    print(Style.RESET_ALL)


start_i = time.time()
for i in range(1000):
    print(equation_levels.get_eq_add_sub_br(i))
    print(equation_levels.get_eq_mul_div_br(i))
    print(equation_levels.get_eq_add_sub_mul_div_br(i))
end_i = time.time()
time_calculate(end_i, start_i)

start_i = time.time()
print(equation_levels.get_eq_add_sub_br(999))
end_i = time.time()
time_calculate(end_i, start_i)

start = time.time()
print(equation_levels.get_eq_mul_div_br(999))
end = time.time()
time_calculate(end, start)

start_i = time.time()
print(equation_levels.get_eq_add_sub_mul_div_br(999))
end_i = time.time()
time_calculate(end_i, start_i)
