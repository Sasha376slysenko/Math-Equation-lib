from config import ConfigGeneralAnalysis
from matplotlib import pyplot as plt
from numpy.typing import NDArray
from typing import ClassVar
from pathlib import Path
from typing import Final
import numpy as np


class PlotHistogram:
    plt.style.use("bmh")
    N_MEASUREMENT: ClassVar[int] = 150

    # Declaration
    # Python Eval
    matrix_cpu_energy_ev: NDArray[np.float32]
    matrix_cpu_load_ev: NDArray[np.float32]
    matrix_cpu_freq_ev: NDArray[np.float32]
    matrix_cpu_temp_ev: NDArray[np.float32]
    matrix_rss_heap_ev: NDArray[np.float32]
    array_rss_ram_ev: NDArray[np.float32]
    # Custom Eval
    matrix_cpu_energy_c_ev: NDArray[np.float32]
    matrix_cpu_load_c_ev: NDArray[np.float32]
    matrix_cpu_freq_c_ev: NDArray[np.float32]
    matrix_cpu_temp_c_ev: NDArray[np.float32]
    matrix_rss_heap_c_ev: NDArray[np.float32]
    matrix_rss_ram_c_ev: NDArray[np.float32]

    def __init__(self) -> None:
        self._config = ConfigGeneralAnalysis()
        self._plot_dir: Path = self._config.plot_dir
        self._list_dir: tuple[str, ...] = self._config.list_dir

        # Init size matrix
        row_el: int = self.N_MEASUREMENT
        n_arch: int = len(self._list_dir)

        # Init MATRIX: Python Eval or Custom Eval
        self.matrix_cpu_energy_ev = np.zeros((n_arch, row_el), dtype=np.float32)
        self.matrix_cpu_load_ev = np.zeros((n_arch, row_el), dtype=np.float32)
        self.matrix_cpu_freq_ev = np.zeros((n_arch, row_el), dtype=np.float32)
        self.matrix_cpu_temp_ev = np.zeros((n_arch, row_el), dtype=np.float32)
        self.matrix_rss_heap_ev = np.zeros((n_arch, row_el), dtype=np.float32)
        self.matrix_rss_ram_ev = np.zeros((n_arch, row_el), dtype=np.float32)
        self.matrix_cpu_energy_c_ev = np.zeros((n_arch, row_el), dtype=np.float32)
        self.matrix_cpu_load_c_ev = np.zeros((n_arch, row_el), dtype=np.float32)
        self.matrix_cpu_freq_c_ev = np.zeros((n_arch, row_el), dtype=np.float32)
        self.matrix_cpu_temp_c_ev = np.zeros((n_arch, row_el), dtype=np.float32)
        self.matrix_rss_heap_c_ev = np.zeros((n_arch, row_el), dtype=np.float32)
        self.matrix_rss_ram_c_ev = np.zeros((n_arch, row_el), dtype=np.float32)

        # Total List link arrays:
        # 1) CPU Load
        # 2) CPU Frequency
        # 3) RSS RAM
        # 4) Heap python
        # 5) CPU Temperature
        # 6) CPU Energy
        self.tuple_python_eval: tuple[NDArray[np.float32], ...] = (
            self.matrix_cpu_load_ev,
            self.matrix_cpu_freq_ev,
            self.matrix_rss_ram_ev,
            self.matrix_rss_heap_ev,
            self.matrix_cpu_temp_ev,
            self.matrix_cpu_energy_ev,
        )
        self.tuple_custom_eval: tuple[NDArray[np.float32], ...] = (
            self.matrix_cpu_load_c_ev,
            self.matrix_cpu_freq_c_ev,
            self.matrix_rss_ram_c_ev,
            self.matrix_rss_heap_c_ev,
            self.matrix_cpu_temp_c_ev,
            self.matrix_cpu_energy_c_ev,
        )

    def _matrix_filling(self) -> None:
        # First Python Eval, second Custom Eval
        metrics: tuple[tuple[NDArray[np.float32], ...], ...] = (
            self.tuple_python_eval,
            self.tuple_custom_eval
        )

        for i, dir_i in enumerate(self._list_dir):
            matrix_file_2d = self._config.file_matrix_2d(dir_i)
            for current, file_1d in zip(metrics, matrix_file_2d):
                for k, file_name in enumerate(file_1d):
                    data = np.loadtxt(
                        file_name, delimiter=",", dtype=np.float32
                    ).ravel()

                    if data.size != self.N_MEASUREMENT:
                        raise ValueError(
                            f"{file_name}: {data.size} != {self.N_MEASUREMENT}"
                        )
                    current[k][i, :] = data


    def _create_plots_hist(self) -> None:
        sqrt_n_mes: float = np.sqrt(self.N_MEASUREMENT)
        x: NDArray = np.arange(len(self._list_dir))
        STEP: Final[int] = 2
        width: float = 0.40
        height: float = 1.5
        counter: int = 0

        # Error style
        err_kw: dict[str, float] = {
            "capsize": 5,
            "capthick": 2,
            "elinewidth": 1.5
        }
        # Labels
        sup_titles: tuple[str, ...] = (
            "CPU Performance",
            "Memory Usage",
            "CPU Thermal & Energy"
        )
        titles_hist: tuple[tuple[str, str], ...] = (
            ("CPU Load (%)", "CPU Frequency (MHz)"),
            ("RSS (MB)", "Heap python (MB)"),
            ("Temperature (°C)", "Energy (J)")
        )
        y_label_log: str = "Logarithmic value"
        y_label: str = "Metric value"
        x_label: str = "Architecture"
        label_1: str = "Python_eval"
        label_2: str = "Custom_eval"
        label_res_1: str | None
        label_res_2: str | None


        for i, (sup_title_i, title_i) in enumerate(zip(sup_titles, titles_hist)):
            fig, axes = plt.subplots(1, 2, figsize=(12, 7))
            plt.suptitle(sup_title_i, fontsize=24, fontweight='bold')

            plot_name: str = sup_title_i.replace(" ", "_")
            axes[0].set_title(title_i[0], fontsize=18)
            axes[1].set_title(title_i[1], fontsize=18)
            axes[0].set_xlabel(x_label, fontsize=16)
            axes[1].set_xlabel(x_label, fontsize=16)
            axes[0].set_ylabel(y_label, fontsize=16)
            axes[1].set_ylabel(y_label, fontsize=16)

            if i == 2:
                axes[1].set_yscale('log')
                axes[1].set_ylabel(y_label_log, fontsize=16)

            # Current Matrix
            matrix_ev_1_i = self.tuple_python_eval[counter]
            matrix_ev_2_i = self.tuple_python_eval[counter+1]
            matrix_c_ev_1_i = self.tuple_custom_eval[counter]
            matrix_c_ev_2_i = self.tuple_custom_eval[counter+1]

            for j, (arch_name, arr_1_ev, arr_2_ev, arr_1_c_ev, arr_2_c_ev) in enumerate(zip(
                    self._list_dir,
                    matrix_ev_1_i,
                    matrix_ev_2_i,
                    matrix_c_ev_1_i,
                    matrix_c_ev_2_i
            )):
                mean_1_ev: float = np.mean(arr_1_ev)
                mean_2_ev: float = np.mean(arr_2_ev)
                mean_1_c_ev: float = np.mean(arr_1_c_ev)
                mean_2_c_ev: float = np.mean(arr_2_c_ev)
                sme_1_ev: float = np.std(arr_1_ev) / sqrt_n_mes
                sme_2_ev: float = np.std(arr_2_ev) / sqrt_n_mes
                sme_1_c_ev: float = np.std(arr_1_c_ev) / sqrt_n_mes
                sme_2_c_ev: float = np.std(arr_2_c_ev) / sqrt_n_mes
                err_low_ev_1: float = np.minimum(mean_1_ev, sme_1_ev)
                err_low_ev_2: float = np.minimum(mean_2_ev, sme_2_ev)
                err_low_c_ev_1: float = np.minimum(mean_1_c_ev, sme_1_c_ev)
                err_low_c_ev_2: float = np.minimum(mean_2_c_ev, sme_2_c_ev)

                # Position BAR: Group BAR
                position_1: float = x[j] - width / 2
                position_2: float = x[j] + width / 2

                # LABELS: Legend figure
                if j == 0:
                    label_res_1 = label_1
                    label_res_2 = label_2
                else:
                    label_res_1 = None
                    label_res_2 = None

                axes[0].bar(position_1, mean_1_ev, width=width, align="center",
                            color="#d95f02", hatch="\\", edgecolor="black",
                            linewidth=2.5, alpha=0.5, label=label_res_1,
                            yerr=[[err_low_ev_1], [sme_1_ev]], error_kw=err_kw)
                axes[0].bar(position_2, mean_1_c_ev, width=width, align="center",
                            color="green", hatch="*", edgecolor="black",
                            linewidth=2.5, alpha=0.5, label=label_res_2,
                            yerr=[[err_low_c_ev_1], [sme_1_c_ev]], error_kw=err_kw)

                axes[1].bar(position_1, mean_2_ev, width=width, align="center",
                            color="#d95f02", hatch="\\", edgecolor="black",
                            linewidth=2.5, alpha=0.5, label=label_res_1,
                            yerr=[[err_low_ev_2], [sme_2_ev]], error_kw=err_kw)
                axes[1].bar(position_2, mean_2_c_ev, width=width, align="center",
                            color="green", hatch="*", edgecolor="black",
                            linewidth=2.5, alpha=0.5, label=label_res_2,
                            yerr=[[err_low_c_ev_2], [sme_2_c_ev]], error_kw=err_kw)

                # Annotation
                diff_1_pct = (1.0 - mean_1_c_ev / mean_1_ev) * 100
                diff_2_pct = (1.0 - mean_2_c_ev / mean_2_ev) * 100

                axes[0].annotate(f"{diff_1_pct:+.1f}%",
                                 xy=(position_2, mean_1_c_ev + height),
                                 ha='center', va='bottom', fontsize=14, fontweight='bold')

                axes[1].annotate(f"{diff_2_pct:+.1f}%",
                                 xy=(position_2, mean_2_c_ev + height),
                                 ha='center', va='bottom', fontsize=14, fontweight='bold')

            # Architecture
            arch_names: list[str] = [
                name.replace("_", " ")
                for name in self._list_dir
            ]

            for ax in axes:
                ax.set_xticks(x)
                ax.set_xticklabels(arch_names, rotation=10, ha="right")
                ax.legend(facecolor="white", edgecolor="black", fontsize=14)
            plt.tight_layout()
            plt.savefig(self._plot_dir / f"{plot_name}.png", dpi=300)
            counter += STEP


    def forward_general_analysis(self) -> None:
        """
        +-----------------------------+
        |Create General Analysis:     |
        |1. Matrix filling.           |
        |2. Create Hist: Mean and STD.|
        +-----------------------------+
        """
        self._matrix_filling()
        self._create_plots_hist()


if __name__ == "__main__":
    plot_hist = PlotHistogram()
    plot_hist.forward_general_analysis()
