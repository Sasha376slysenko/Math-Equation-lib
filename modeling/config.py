import os
import re
import platform
import subprocess
from pathlib import Path
from typing import ClassVar
from dataclasses import dataclass, field


def replace_platform(model: str) -> str:
    slug: str = re.sub(
        r'[^a-zA-Z0-9]+',
        '_', model
    ).strip().lower()
    return slug


"""
Detected architecture:
+---------------------------+
|1. System OS.              |
|2. Machine.                |
|3. IF OS.                  |
|4. MacOS, Linux, UnknownOS.|
|5. CPU info.               |
+---------------------------+
"""
def detect_architecture() -> str:
    result_platform: str
    system = platform.system().lower()
    machine = platform.machine().lower()

    if system == "darwin":
        try:
            brand: str = subprocess.check_output([
                "sysctl", "-n", "machdep.cpu.brand_string"
            ]).decode().strip()
            return replace_platform(brand)
        except Exception:
            return f"apple_{machine}"

    elif system == "linux":
        try:
            with open("/proc/cpuinfo", "r") as file:
                for line in file:
                    if "model name" in line:
                        model: str = line.split(":")[1].strip()
                        return replace_platform(model)
        except Exception:
            pass

        return f"linux_{machine}"
    return f"unknown_{system}_{machine}"


@dataclass
class Config:
    arch_name: str = field(default_factory=detect_architecture)
    BASE_DIR: Path = field(default_factory=lambda: Path(__file__).parent)

    # Dynamic filed
    SAVE_DIR_PLOT: Path = field(init=False)
    SAVE_DIR_DATA_EV: Path = field(init=False)
    SAVE_DIR_DATA_C_EV: Path = field(init=False)

    file_py_heap_ev: str = field(init=False)
    file_ram_uss_ev: str = field(init=False)
    file_ram_rss_ev: str = field(init=False)
    file_cpu_load_ev: str = field(init=False)
    file_cpu_freq_ev: str = field(init=False)
    file_cpu_temp_ev: str = field(init=False)
    file_cpu_energy_ev: str = field(init=False)

    file_py_heap_c_ev: str = field(init=False)
    file_ram_uss_c_ev: str = field(init=False)
    file_ram_rss_c_ev: str = field(init=False)
    file_cpu_load_c_ev: str = field(init=False)
    file_cpu_freq_c_ev: str = field(init=False)
    file_cpu_temp_c_ev: str = field(init=False)
    file_cpu_energy_c_ev: str = field(init=False)

    plot_ram_use: str = field(init=False)
    plot_cpu_use: str = field(init=False)
    plot_total_res: str = field(init=False)
    plot_cpu_energy_use: str = field(init=False)
    plot_cpu_use_temp_profile: str = field(init=False)

    def __post_init__(self):
        # save dir
        self.SAVE_DIR_PLOT = self.BASE_DIR / 'results' / self.arch_name
        self.SAVE_DIR_DATA_EV = self.BASE_DIR / 'data' / self.arch_name / 'python_eval'
        self.SAVE_DIR_DATA_C_EV = self.BASE_DIR / 'data' / self.arch_name / 'custom_eval'

        # Automatically make dir
        self.SAVE_DIR_PLOT.mkdir(parents=True, exist_ok=True)
        self.SAVE_DIR_DATA_EV.mkdir(parents=True, exist_ok=True)
        self.SAVE_DIR_DATA_C_EV.mkdir(parents=True, exist_ok=True)

        # Data export python eval
        self.file_py_heap_ev = os.path.join(self.SAVE_DIR_DATA_EV, "py_heap_ev.csv")
        self.file_ram_uss_ev = os.path.join(self.SAVE_DIR_DATA_EV, "ram_uss_ev.csv")
        self.file_ram_rss_ev = os.path.join(self.SAVE_DIR_DATA_EV, "ram_rss_ev.csv")
        self.file_cpu_load_ev = os.path.join(self.SAVE_DIR_DATA_EV, "cpu_load_ev.csv")
        self.file_cpu_freq_ev = os.path.join(self.SAVE_DIR_DATA_EV, "cpu_freq_ev.csv")
        self.file_cpu_temp_ev = os.path.join(self.SAVE_DIR_DATA_EV, "cpu_temp_ev.csv")
        self.file_cpu_energy_ev = os.path.join(self.SAVE_DIR_DATA_EV, "cpu_energy_ev.csv")

        # Data export custom eval
        self.file_py_heap_c_ev = os.path.join(self.SAVE_DIR_DATA_C_EV, "py_heap_c_ev.csv")
        self.file_ram_uss_c_ev = os.path.join(self.SAVE_DIR_DATA_C_EV, "ram_uss_c_ev.csv")
        self.file_ram_rss_c_ev = os.path.join(self.SAVE_DIR_DATA_C_EV, "ram_rss_c_ev.csv")
        self.file_cpu_load_c_ev = os.path.join(self.SAVE_DIR_DATA_C_EV, "cpu_load_c_ev.csv")
        self.file_cpu_freq_c_ev = os.path.join(self.SAVE_DIR_DATA_C_EV, "cpu_freq_c_ev.csv")
        self.file_cpu_temp_c_ev = os.path.join(self.SAVE_DIR_DATA_C_EV, "cpu_temp_c_ev.csv")
        self.file_cpu_energy_c_ev = os.path.join(self.SAVE_DIR_DATA_C_EV, "cpu_energy_c_ev.csv")

        # Plot graphs
        self.plot_ram_use = os.path.join(self.SAVE_DIR_PLOT, "ram_used.png")
        self.plot_cpu_use = os.path.join(self.SAVE_DIR_PLOT, "cpu_used.png")
        self.plot_total_res = os.path.join(self.SAVE_DIR_PLOT, "total_res.png")
        self.plot_cpu_energy_use = os.path.join(self.SAVE_DIR_PLOT, "cpu_energy_used.png")
        self.plot_cpu_use_temp_profile = os.path.join(self.SAVE_DIR_PLOT, "hardware_3d_profile.png")


@dataclass(frozen=True)
class ConfigGeneralAnalysis:
    BASE_DIR: Path = Path(__file__).parent

    # CONSTS
    DIR_DATA_CSV: ClassVar[tuple[str, ...]] = (
        "python_eval", "custom_eval"
    )
    FILE_MATRIX_2D: ClassVar[tuple[tuple[str, ...], ...]] = (
        (
            "cpu_load_ev.csv", "cpu_freq_ev.csv",
            "ram_rss_ev.csv", "py_heap_ev.csv",
            "cpu_temp_ev.csv", "cpu_energy_ev.csv"
        ),
        (
            "cpu_load_c_ev.csv", "cpu_freq_c_ev.csv",
            "ram_rss_c_ev.csv", "py_heap_c_ev.csv",
            "cpu_temp_c_ev.csv", "cpu_energy_c_ev.csv"
        )
    )


    @property
    def base_dir_data(self) -> Path:
        return self.BASE_DIR / 'data'


    @property
    def plot_dir(self) -> Path:
        return self.BASE_DIR / 'results' / 'general_results'


    @property
    def list_dir(self) -> tuple[str, ...]:
        return tuple(
            entry.name
            for entry in self.base_dir_data.iterdir()
            if entry.is_dir()
        )


    @staticmethod
    def _full_name_file_dir(dir_name: Path,
                            dir_csv: str,
                            file_name: tuple[str, ...]
                            ) -> tuple[Path, ...]:
        return tuple(
            'data' / dir_name / dir_csv / file_name_i
            for file_name_i in file_name
        )


    def file_matrix_2d(self,
                       dir_name: str
                       ) -> tuple[tuple[Path, ...], tuple[Path, ...]]:
        # Path dir DATA
        data_dir: Path = Path(dir_name)

        # RESULT Dir file data -> MATRIX 2D
        return tuple(
            self._full_name_file_dir(data_dir, dir_csv, f_name)
            for dir_csv, f_name in zip(self.DIR_DATA_CSV, self.FILE_MATRIX_2D)
        )
