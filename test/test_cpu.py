import numpy as np
from matplotlib import pyplot as plt

data_custom_eval = np.genfromtxt('test/data_cpu/custom_eval_generation_eq.csv', delimiter=',', dtype=None, encoding='utf-8', names=True)
data_python_eval = np.genfromtxt('test/data_cpu/python_eval_generation_eq.csv', delimiter=',', dtype=None, encoding='utf-8', names=True)

# print console title csv
for i, title in enumerate(data_custom_eval.dtype.names):
    print(f"{i+1}.title_csv: {title}")

# CUSTOM EVAL
time_custom_eval: np.ndarray = data_custom_eval['Elapsed_Time_sec']
energy_custom: np.ndarray = data_custom_eval['Cumulative_Processor_Energy_0mWh']
power_custom: np.ndarray = data_custom_eval['Processor_Power_0Watt']
cpu_utilization_custom: np.ndarray = data_custom_eval['CPU_Utilization']
package_temperature_custom: np.ndarray = data_custom_eval['Package_Temperature_0C']

#  EVAL PYTHON
time_python_eval = data_python_eval['Elapsed_Time_sec']
energy_python: np.ndarray = data_python_eval['Cumulative_Processor_Energy_0mWh']
power_python: np.ndarray = data_python_eval['Processor_Power_0Watt']
cpu_utilization_python: np.ndarray = data_python_eval['CPU_Utilization']
package_temperature_python: np.ndarray = data_python_eval['Package_Temperature_0C']


"""
    +---------------------------------------+
    | Create plot func (np.ndarray[MATRIX]) |
    +---------------------------------------+
"""
def create_plot(titles: list[str], labels: list[str], y_label: str, axes: np.ndarray, filename: str) -> None:
    fig = plt.figure(figsize=(19, 23))
    # create ax_...
    ax_1 = fig.add_subplot(3, 1, 1)
    ax_2 = fig.add_subplot(3, 1, 2)
    ax_3 = fig.add_subplot(3, 1, 3)
    # title ax_...
    ax_1.set_title(titles[0], fontsize=16)
    ax_2.set_title(titles[1], fontsize=16)
    ax_3.set_title(titles[2], fontsize=16)
    # x label ax_...
    ax_1.set_xlabel('Elapsed Time (sec)', fontsize=14)
    ax_2.set_xlabel('Elapsed Time (sec)', fontsize=14)
    # y label ax_...
    ax_1.set_ylabel(y_label, fontsize=14)
    ax_2.set_ylabel(y_label, fontsize=14)
    ax_3.set_ylabel(y_label, fontsize=14)
    ax_3.grid()
    # plot ax_...
    ax_1.plot(time_python_eval, axes[0], color="red", linewidth=3, label=labels[0])
    ax_2.plot(time_custom_eval, axes[1], color="green", linewidth=3, label=labels[1])
    bplot = ax_3.boxplot(
        [np.ravel(axes[0]), np.ravel(axes[1])],
        patch_artist=True,
        tick_labels=['eval', 'custom eval']
    )
    plt.savefig(f'res_test_cpu/{filename}.png', dpi=300)


if __name__ == '__main__':
    y_label_1: str = 'Cumulative_Processor_Energy_0mWh'
    y_label_2: str = 'Processor_Power_0Watt'
    y_label_3: str = 'CPU_Utilization(%)'
    y_label_4: str = 'Package_Temperature_0C'

    title_1: str = 'Енергоспоживання з часом'
    title_2: str = 'Миттєва потужність процесора'
    title_3: str = 'Завантаження CPU'
    title_4: str = 'Температура процесора'

    title_1_plot: list[str] = [title_1+' (eval)', title_1+' (custom eval)', title_1+' (eval vs custom eval)']
    title_2_plot: list[str] = [title_2+' (eval)', title_2+' (custom eval)', title_2+' (eval vs custom eval)']
    title_3_plot: list[str] = [title_3+' (eval)', title_3+' (custom eval)', title_3+' (eval vs custom eval)']
    title_4_plot: list[str] = [title_4+' (eval)', title_4+' (custom eval)', title_4+' (eval vs custom eval)']

    create_plot(title_1_plot, ['eval', 'custom eval'], y_label_1, [energy_python, energy_custom], title_1)
    create_plot(title_2_plot, ['eval', 'custom eval'], y_label_2, [power_python, power_custom], title_2)
    create_plot(title_3_plot, ['eval', 'custom eval'], y_label_3, [cpu_utilization_python, cpu_utilization_custom], title_3)
    create_plot(title_4_plot, ['eval', 'custom eval'], y_label_4, [package_temperature_python, package_temperature_custom], title_4)