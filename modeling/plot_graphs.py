from matplotlib import pyplot as plt
from dict_in_for import DictDigits
from numpy.typing import NDArray
from config import Config
import numpy as np

"""
+---------------------------------------------+
|Model telemetry:                             |
|1. Create matrix. Declaration -> Init.       |
|2. Create dict[path: link_variable].         |
|2. Read DATA. Itr -> Matrix -> link_variable.|
+---------------------------------------------+
"""
class DataRead:
    # CPU DATA:
    matrix_cpu_load_eval: NDArray[np.float64]
    matrix_cpu_freq_eval: NDArray[np.float64]
    matrix_cpu_temp_eval: NDArray[np.float64]
    matrix_cpu_energy_eval: NDArray[np.float64]
    matrix_cpu_load_c_eval: NDArray[np.float64]
    matrix_cpu_freq_c_eval: NDArray[np.float64]
    matrix_cpu_temp_c_eval: NDArray[np.float64]
    matrix_cpu_energy_c_eval: NDArray[np.float64]

    # RAM DATA:
    matrix_ram_rss_eval: NDArray[np.float64]
    matrix_ram_uss_eval: NDArray[np.float64]
    matrix_py_heap_eval: NDArray[np.float64]
    matrix_ram_rss_c_eval: NDArray[np.float64]
    matrix_ram_uss_c_eval: NDArray[np.float64]
    matrix_py_heap_c_eval: NDArray[np.float64]

    def __init__(self):
        self._config = Config()
        self._read_data()

    def _read_data(self) -> None:
        results: dict[str, str] = {
            **{
                self._config.file_cpu_load_ev: "matrix_cpu_load_eval",
                self._config.file_cpu_freq_ev: "matrix_cpu_freq_eval",
                self._config.file_cpu_temp_ev: "matrix_cpu_temp_eval",
                self._config.file_ram_rss_ev: "matrix_ram_rss_eval",
                self._config.file_ram_uss_ev: "matrix_ram_uss_eval",
                self._config.file_py_heap_ev: "matrix_py_heap_eval",
                self._config.file_cpu_energy_ev: "matrix_cpu_energy_eval"
            },
            **{
                self._config.file_cpu_load_c_ev: "matrix_cpu_load_c_eval",
                self._config.file_cpu_freq_c_ev: "matrix_cpu_freq_c_eval",
                self._config.file_cpu_temp_c_ev: "matrix_cpu_temp_c_eval",
                self._config.file_ram_rss_c_ev: "matrix_ram_rss_c_eval",
                self._config.file_ram_uss_c_ev: "matrix_ram_uss_c_eval",
                self._config.file_py_heap_c_ev: "matrix_py_heap_c_eval",
                self._config.file_cpu_energy_c_ev: "matrix_cpu_energy_c_eval"
            }
        }

        for file, name_matrix in results.items():
            setattr(self, name_matrix, np.loadtxt(file, delimiter=",", dtype=np.float64))


"""
|Model telemetry: |
|1. |
|2. |
|3. |
"""
class PlotGraphs:
    WIDTH_PLOT: int = 13
    HEIGHT_PLOT: int = 15

    # Declaration: digits
    _tuple_digits: tuple[str, ...]

    # Declaration: RAM DATA
    _arr_ram_rss_eval: NDArray[np.float64]
    _arr_ram_uss_eval: NDArray[np.float64]
    _arr_py_heap_eval: NDArray[np.float64]
    _arr_ram_rss_c_eval: NDArray[np.float64]
    _arr_ram_uss_c_eval: NDArray[np.float64]
    _arr_py_heap_c_eval: NDArray[np.float64]

    # Declaration: CPU DATA
    _arr_cpu_load_eval: NDArray[np.float64]
    _arr_cpu_freq_eval: NDArray[np.float64]
    _arr_cpu_temp_eval: NDArray[np.float64]
    _arr_cpu_energy_eval: NDArray[np.float64]
    _arr_cpu_load_c_eval: NDArray[np.float64]
    _arr_cpu_freq_c_eval: NDArray[np.float64]
    _arr_cpu_temp_c_eval: NDArray[np.float64]
    _arr_cpu_energy_c_eval: NDArray[np.float64]
    _arr_energy_state_eval: NDArray[np.float64]
    _arr_energy_state_c_eval: NDArray[np.float64]
    _arr_cpu_load_eval_all: NDArray[np.float64]
    _arr_cpu_load_c_eval_all: NDArray[np.float64]
    _arr_cpu_freq_eval_all: NDArray[np.float64]
    _arr_cpu_freq_c_eval_all: NDArray[np.float64]
    _arr_cpu_energy_eval_all: NDArray[np.float64]
    _arr_cpu_energy_c_eval_all: NDArray[np.float64]

    def __init__(self):
        self._config = Config()
        self._data_read = DataRead()
        self._dict_digits = DictDigits()

        # Init data RAM
        self._arr_ram_rss_eval = self._data_read.matrix_ram_rss_eval[0]
        self._arr_ram_uss_eval = self._data_read.matrix_ram_uss_eval[0]
        self._arr_py_heap_eval = self._data_read.matrix_py_heap_eval[0]
        self._arr_ram_rss_c_eval = self._data_read.matrix_ram_rss_c_eval[0]
        self._arr_ram_uss_c_eval = self._data_read.matrix_ram_uss_c_eval[0]
        self._arr_py_heap_c_eval = self._data_read.matrix_py_heap_c_eval[0]

        # Init data CPU
        self._tuple_digits = self._dict_digits.dict_digits_4["4-generation-equation-1"]
        self._arr_cpu_load_eval = self._data_read.matrix_cpu_load_eval[0]
        self._arr_cpu_freq_eval = self._data_read.matrix_cpu_freq_eval[0]
        self._arr_cpu_temp_eval = self._data_read.matrix_cpu_temp_eval[0]
        self._arr_cpu_energy_eval = self._data_read.matrix_cpu_energy_eval[0]
        self._arr_cpu_load_c_eval = self._data_read.matrix_cpu_load_c_eval[0]
        self._arr_cpu_freq_c_eval = self._data_read.matrix_cpu_freq_c_eval[0]
        self._arr_cpu_temp_c_eval = self._data_read.matrix_cpu_temp_c_eval[0]
        self._arr_cpu_energy_c_eval = self._data_read.matrix_cpu_energy_c_eval[0]
        self._arr_energy_state_eval = self._arr_cpu_load_eval * self._arr_cpu_freq_eval
        self._arr_energy_state_c_eval = self._arr_cpu_load_c_eval * self._arr_cpu_freq_c_eval

        # Init data CPU Load All
        self._arr_cpu_load_eval_all = self._data_read.matrix_cpu_load_eval.flatten()
        self._arr_cpu_load_c_eval_all = self._data_read.matrix_cpu_load_c_eval.flatten()

        # Init data CPU Freq All
        self._arr_cpu_freq_eval_all = self._data_read.matrix_cpu_freq_eval.flatten()
        self._arr_cpu_freq_c_eval_all = self._data_read.matrix_cpu_freq_c_eval.flatten()

        # Init data CPU Energy ALL
        self._arr_cpu_energy_eval_all = self._data_read.matrix_cpu_energy_eval.flatten()
        self._arr_cpu_energy_c_eval_all = self._data_read.matrix_cpu_energy_c_eval.flatten()

        # Init dict DATA
        self.data: dict[str, tuple[str, ...] | NDArray[np.float64]] = {
            "digits": self._tuple_digits,
            "cpu_load_ev": self._arr_cpu_load_eval,
            "cpu_freq_ev": self._arr_cpu_freq_eval,
            "cpu_temp_ev": self._arr_cpu_temp_eval,
            "cpu_energy_ev": self._arr_cpu_energy_eval,
            "ram_rss_ev": self._arr_ram_rss_eval,
            "ram_uss_ev": self._arr_ram_uss_eval,
            "py_heap_ev": self._arr_py_heap_eval,
            "cpu_load_ev_all": self._arr_cpu_load_eval_all,
            "cpu_freq_ev_all": self._arr_cpu_freq_eval_all,
            "cpu_energy_ev_all": self._arr_cpu_energy_eval_all,

            "cpu_load_c_ev": self._arr_cpu_load_c_eval,
            "cpu_freq_c_ev": self._arr_cpu_freq_c_eval,
            "cpu_temp_c_ev": self._arr_cpu_temp_c_eval,
            "cpu_energy_c_ev": self._arr_cpu_energy_c_eval,
            "energy_state_ev": self._arr_energy_state_eval,
            "energy_state_c_ev": self._arr_energy_state_c_eval,
            "ram_rss_c_ev": self._arr_ram_rss_c_eval,
            "ram_uss_c_ev": self._arr_ram_uss_c_eval,
            "py_heap_c_ev": self._arr_py_heap_c_eval,
            "cpu_load_c_ev_all": self._arr_cpu_load_c_eval_all,
            "cpu_freq_c_ev_all": self._arr_cpu_freq_c_eval_all,
            "cpu_energy_c_ev_all": self._arr_cpu_energy_c_eval_all,
        }


    @staticmethod
    def _providing_styles(axes: tuple,
                          titles: tuple[str, ...],
                          labels_x: tuple[str, ...],
                          labels_y: tuple[str, ...],
                          label_z: tuple[str, ...] | None = None,
                          flag_axis: bool=False, flag_rotate: bool=True) -> None:
        for i, (ax, title, label_y, label_x) in enumerate(zip(
                axes, titles, labels_y, labels_x
        )):
            if not flag_axis:
                ax.legend(
                    fontsize=16,
                    loc='best',
                    edgecolor='black',
                    facecolor='white'
                )

            ax.set_title(title, fontsize=16)
            ax.set_ylabel(label_y, fontsize=14)
            ax.set_xlabel(label_x, fontsize=14)

            if flag_axis and label_z is not None:
                try:
                    ax.set_zlabel(label_z[i], fontsize=14)
                except AttributeError:
                    pass

            if flag_rotate:
                ax.tick_params(axis="x", labelrotation=70)


    def _analysis_ram_used(self) -> None:
        plt.style.use("bmh")
        fig = plt.figure(figsize=(self.WIDTH_PLOT, self.HEIGHT_PLOT))

        ax_1 = fig.add_subplot(3, 1, 1)
        ax_2 = fig.add_subplot(3, 1, 2)
        ax_3 = fig.add_subplot(3, 1, 3)
        axes = (ax_1, ax_2, ax_3)

        label_1: str = "Heap: python_eval"
        label_3: str = "RAM RSS: python_eval"
        label_5: str = "RAM USS: python_eval"
        label_2: str = "Heap: custom_eval"
        label_4: str = "RAM RSS: custom_eval"
        label_6: str = "RAM USS: custom_eval"
        sup_title: str = "Analysis of memory consumption"

        titles: tuple[str, ...] = (
            "Python Interpreter Heap Consumption",
            "Resident Set Size (RSS) Overhead",
            "Unique Set Size (USS) Resource Footprint"
        )
        labels_x: tuple[str, ...] = (
            "Target Digit Tokens",
            "Target Digit Tokens",
            "Target Digit Tokens"
        )
        labels_y: tuple[str, ...] = (
            "Memory Allocated (KB)",
            "Memory Size (MB)",
            "Memory Size (MB)"
        )

        # Python interpretation heap
        ax_1.plot(self.data["digits"], self.data["py_heap_ev"],
                  label=label_1, color="red", linewidth=3,
                  marker="*", markersize=8)
        ax_1.plot(self.data["digits"], self.data["py_heap_c_ev"],
                  label=label_2, color="green", linewidth=3,
                  marker="o", markersize=8)

        # RAM RSS
        ax_2.plot(self.data["digits"], self.data["ram_rss_ev"],
                  label=label_3, color="red", marker="*",
                  linewidth=3, markersize=8)
        ax_2.plot(self.data["digits"], self.data["ram_rss_c_ev"],
                  label=label_4, color="green", marker="o",
                  linewidth=3, markersize=8)

        # RAM USS
        ax_3.plot(self.data["digits"], self.data["ram_uss_ev"],
                  label=label_5, color="red", marker="*",
                  linewidth=3, markersize=8)
        ax_3.plot(self.data["digits"], self.data["ram_uss_c_ev"],
                  label=label_6, color="green", marker="o",
                  linewidth=3, markersize=8)

        self._providing_styles(axes, titles, labels_x, labels_y)
        plt.suptitle(sup_title, fontsize=24, fontweight="bold")
        plt.tight_layout()
        plt.savefig(self._config.plot_ram_use, dpi=300)
        plt.close()


    def _analysis_cpu_used(self) -> None:
        plt.style.use("bmh")
        fig = plt.figure(figsize=(self.WIDTH_PLOT, self.HEIGHT_PLOT))

        ax_1 = fig.add_subplot(3, 1, 1)
        ax_2 = fig.add_subplot(3, 1, 2)
        ax_3 = fig.add_subplot(3, 1, 3)
        axes = (ax_1, ax_2, ax_3)

        sup_title: str = "Analysis of CPU usage"
        label_1: str = "CPU Freq: python_eval"
        label_2: str = "CPU Freq: custom_eval"
        label_3: str = "Python_eval()"
        label_4: str = "Custom_eval()"

        labels_x: tuple[str, ...] = (
            "Execution Profile",
            "Target Digit Tokens",
            "CPU Frequency (MHz)"
        )
        labels_y: tuple[str, ...] = (
            "CPU Utilization (%)",
            "Frequency (MHz)",
            "CPU Utilization / Load (%)"
        )
        titles: tuple[str, ...] = (
            "Statistical Distribution of CPU Load (BoxPlot)",
            "Dynamic CPU Frequency Scaling Tracking",
            "CPU Operating States: Frequency vs Load"
        )

        # CPU Load
        box_data = [
            np.ravel(self.data["cpu_load_ev_all"]),
            np.ravel(self.data["cpu_load_c_ev_all"])
        ]
        bp = ax_1.boxplot(
            box_data,
            notch=True,
            patch_artist=True,
            label=["Python_eval()", "Custom_eval()"]
        )
        colors = ["#d62728", "#2ca02c"]

        for patch, color in zip(bp["boxes"], colors):
            patch.set_facecolor(color)
            patch.set_alpha(0.8)

        for path in bp["medians"]:
            path.set(color="black", linewidth=2, linestyle="--")

        # CPU Freq
        ax_2.plot(self.data["digits"], self.data["cpu_freq_ev"],
                  label=label_1, color="red", marker="*",
                  linewidth=3, markersize=8)
        ax_2.plot(self.data["digits"], self.data["cpu_freq_c_ev"],
                  label=label_2, color="green", marker="o",
                  linewidth=3, markersize=8)

        # CPU Load vs Freq
        ax_3.scatter(self.data["cpu_freq_ev_all"], self.data["cpu_load_ev_all"],
                  label=label_3, color="red", marker="*", s=120)
        ax_3.scatter(self.data["cpu_freq_c_ev_all"], self.data["cpu_load_c_ev_all"],
                  label=label_4, color="green", marker="o", s=120)

        self._providing_styles(axes, titles, labels_x, labels_y)
        plt.suptitle(sup_title, fontsize=23, fontweight="bold")
        plt.tight_layout()
        plt.savefig(self._config.plot_cpu_use, dpi=300)
        plt.close()


    def _analysis_cpu_energy_used(self):
        plt.style.use("bmh")
        fig = plt.figure(figsize=(self.WIDTH_PLOT, self.HEIGHT_PLOT))

        ax_1 = fig.add_subplot(3, 1, 1)
        ax_2 = fig.add_subplot(3, 1, 2)
        ax_3 = fig.add_subplot(3, 1, 3)
        axes = (ax_1, ax_2, ax_3)

        sup_title: str = "Analysis of energy efficiency of processor use"
        label_1: str = "Direct Energy: python_eval"
        label_2: str = "State Stress: python_eval"
        label_3: str = "Direct Energy: custom_eval"
        label_4: str = "State Stress: custom_eval"
        label_5: str = "Temperature: Python_eval()"
        label_6: str = "Temperature: Custom_eval()"

        labels_x: tuple[str, ...] = (
            "Target Digit Tokens",
            "Target Digit Tokens",
            "Target Digit Tokens"
        )
        labels_y: tuple[str, ...] = (
            "Energy Dissipation (Joules)",
            "Stress Index (Arbitrary Units)",
            "CPU Temperature Package id 0"
        )
        titles: tuple[str, ...] = (
            "Hardware CPU Energy Consumption via Intel RAPL",
            "Mathematical Energy State Proxy ($Load \\times Freq$)",
            "Temperature Python_eval() vs Custom_eval()"
        )

        # CPU: energy
        ax_1.plot(self.data["digits"], self.data["cpu_energy_ev"],
                  label=label_1, color="red", linewidth=3,
                  marker="*", markersize=8)
        ax_1.plot(self.data["digits"], self.data["cpu_energy_c_ev"],
                  label=label_2, color="green", linewidth=3,
                  marker="o", markersize=8)

        # Energy state
        ax_2.plot(self.data["digits"], self.data["energy_state_ev"],
                  label=label_3, color="red", marker="*",
                  linewidth=3, markersize=8)
        ax_2.plot(self.data["digits"], self.data["energy_state_c_ev"],
                  label=label_4, color="green", marker="o",
                  linewidth=3, markersize=8)

        # CPU: temperature
        ax_3.plot(self.data["digits"], self.data["cpu_temp_ev"],
                  label=label_5, color="red", marker="*",
                  linewidth=3, markersize=8)

        ax_3.plot(self.data["digits"], self.data["cpu_temp_c_ev"],
                  label=label_6, color="green", marker="o",
                  linewidth=3, markersize=8)

        self._providing_styles(axes, titles, labels_x, labels_y)
        plt.suptitle(sup_title, fontsize=24, fontweight="bold")
        plt.tight_layout()
        plt.savefig(self._config.plot_cpu_energy_use, dpi=300)
        plt.close()


    def _analysis_3d_scatter(self):
        plt.style.use("bmh")
        fig = plt.figure(figsize=(15, 7))

        ax_1 = fig.add_subplot(121, projection="3d")
        ax_2 = fig.add_subplot(122, projection="3d")
        axes_3d = (ax_1, ax_2)

        x_ev = self.data["cpu_load_ev_all"]
        y_ev = self.data["cpu_freq_ev_all"]
        z_ev = self.data["cpu_energy_ev_all"]

        x_c_ev = self.data["cpu_load_c_ev_all"]
        y_c_ev = self.data["cpu_freq_c_ev_all"]
        z_c_ev = self.data["cpu_energy_c_ev_all"]


        titles: tuple[str, ...] = (
            "Standard python_eval() 3D State Space",
            "Optimized custom_eval() 3D State Space"
        )
        labels_z: tuple[str, ...] = (
            "Hardware Energy",
            "Hardware Energy"
        )
        labels_y: tuple[str, ...] = (
            "CPU Frequency (MHz)",
            "CPU Frequency (MHz)"
        )
        labels_x: tuple[str, ...] = (
            "CPU Load (%)",
            "CPU Load (%)"
        )

        # Python interpretation eval()
        ax_1.scatter3D(x_ev, y_ev, z_ev, c=z_ev, cmap="jet", s=50)
        ax_1.view_init(elev=20, azim=60)

        # Custom eval()
        ax_2.scatter3D(x_c_ev, y_c_ev, z_c_ev, c=z_c_ev, cmap="jet", s=50)
        ax_2.view_init(elev=20, azim=60)

        self._providing_styles(
            axes_3d, titles, labels_x,
            labels_y, labels_z,
            flag_rotate=False,
            flag_axis=True
        )
        plt.tight_layout()
        plt.savefig(self._config.plot_cpu_use_temp_profile, dpi=300)
        plt.close()


    def forward_analysis(self) -> None:
        self._analysis_ram_used()
        self._analysis_cpu_used()
        self._analysis_3d_scatter()
        self._analysis_cpu_energy_used()
