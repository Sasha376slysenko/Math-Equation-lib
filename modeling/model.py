from math_core.python_api.equation_lib_cpp import EquationConfig as CustomConfig
from math_core.python_api.equation_lib_cpp import EvalEquation as CustomEval
from math_core.python_api.eq_eval import EquationConfig
from math_core.python_api.eq_eval import EvalEquation
from abc import ABC, abstractmethod
from dict_in_for import DictDigits
from numpy.typing import NDArray
from config import Config
from pathlib import Path
from typing import Final

import os
import re
import time
import psutil
import threading
import subprocess
import numpy as np
import tracemalloc


class BaseTelemetry(ABC):
    @abstractmethod
    def reset_baseline(self) -> None:
        """Оновлення енергій телеметрії"""
        pass

    @abstractmethod
    def get_cpu_load(self) -> float:
        """Повертає поточне навантаження процесора"""
        pass

    @abstractmethod
    def get_cpu_freq(self) -> float:
        """Повертає поточну частоту процесора"""
        pass

    @abstractmethod
    def get_cpu_temp(self) -> float:
        """Повертає поточну температуру процесора"""
        pass

    @abstractmethod
    def get_cpu_energy(self) -> float:
        """Повертає поточне енергоспоживання процесора"""
        pass

    @abstractmethod
    def get_ram_rss(self) -> float:
        """Повертає фізичне використання RAM"""
        pass

    @abstractmethod
    def get_ram_uss(self) -> float:
        """Повертає унікальне використання RAM"""
        pass


"""
+------------------------------------+
|Modern intel{9-13} linux telemetry: |
|1. Measurement RAM RSS.             |
|2. Measurement RAM USS.             |
|3. Measurement CPU LOAD.            |
|4. Measurement CPU FREQ.            |
|5. Measurement CPU TEMP.            |
|6. Measurement CPU ENERGY.          |
+------------------------------------+
"""
class ModernIntelLinuxTelemetry(BaseTelemetry):
    def __init__(self) -> None:
        self._process = psutil.Process(os.getpid())
        self._warmup()

        # Delta energy CPU
        self._last_energy_uj: float = 0.0
        self._acc_energy_j_cpu: float = 0.0

        # CONSTS: B_to_MB, CPU: sensor
        self._CPU_SENSOR: Final[str] = "coretemp"
        self._CPU_LABEL: Final[str] = "Package id 0"
        self._uj_to_j: Final[float] = 1_000_000.0
        self._max_uj: Final[float] = 4_294_967_295.0
        self._path: Final[str] = "/sys/class/powercap/intel-rapl:0/energy_uj"

        # Start measurement
        self.reset_baseline()


    def _warmup(self) -> None:
        self._process.cpu_percent(interval=3)

    def _current_cpu_temperature(self) -> float:
        cpu_temp = psutil.sensors_temperatures()
        for sensor in cpu_temp.get(self._CPU_SENSOR, []):
            if sensor.label == self._CPU_LABEL:
                return sensor.current
        return 0.0

    def _read_cpu_energy(self) -> float:
        try:
            return float(Path(self._path).read_text())
        except PermissionError:
            return 0.0
        except FileNotFoundError:
            return 0.0

    def _stop_measure(self) -> float:
        curr_energy_uj: float = self._read_cpu_energy()

        if curr_energy_uj >= self._last_energy_uj:
            delta_uj: float = curr_energy_uj - self._last_energy_uj
        else:
            delta_uj: float = (self._max_uj - self._last_energy_uj) + curr_energy_uj

        self._acc_energy_j_cpu += delta_uj / self._uj_to_j
        self._last_energy_uj = curr_energy_uj
        return self._acc_energy_j_cpu


    # SETTER
    def reset_baseline(self) -> None:
        self._acc_energy_j_cpu = 0.0
        self._last_energy_uj = self._read_cpu_energy()

    # GETTERS
    def get_cpu_load(self) -> float:
        return self._process.cpu_percent(interval=0)

    def get_cpu_freq(self) -> float:
        freq = psutil.cpu_freq()
        return freq.current if freq else 0.0

    def get_cpu_temp(self) -> float:
        return self._current_cpu_temperature()

    def get_cpu_energy(self) -> float:
        return self._stop_measure()

    def get_ram_rss(self) -> float:
        return self._process.memory_full_info().rss

    def get_ram_uss(self) -> float:
        return self._process.memory_full_info().uss


"""
+---------------------------------------------------------+
|Legacy intel{1-2} linux telemetry:                       |
|1. Measurement RAM RSS.                                  |
|2. Measurement RAM USS.                                  |
|3. Measurement CPU LOAD.                                 |
|4. Measurement CPU FREQ.                                 |
|5. Measurement CPU TEMP -> Package id 0 or Max temp core.|
|6. Measurement CPU ENERGY -> Battery or Int cpu energy.  |
+---------------------------------------------------------+
"""
class LegacyIntelLinuxTelemetry(BaseTelemetry):
    def __init__(self, tdp_watts: float = 35.0) -> None:
        self._process = psutil.Process(os.getpid())
        self._warmup()

        # Accumulation energy joules
        self._acc_energy_j_cpu: float = 0.0

        # Energy = Power * dt, dt -> time_i - start_time
        self._last_time: float = time.perf_counter()

        # CONSTS: B_TO_MB, BATTERY: sensor
        self._tdp: Final[float] = tdp_watts
        self._CPU_SENSOR: Final[str] = "coretemp"
        self._CPU_LABEL: Final[str] = "Package id 0"
        self._uw_to_w: Final[float] = 1_000_000.0
        self._bat_file: Final[str] = "/sys/class/power_supply/BAT0/power_now"


    def _warmup(self) -> None:
        self._process.cpu_percent(interval=3)

    def _current_cpu_temperature(self) -> float:
        """
        +-------------------------------------------------------+
        |1. Read low level counter -> psutil -> sensors.        |
        |2. Read sysfs -> /sys/class/thermal/thermal_zone0/temp.|
        +-------------------------------------------------------+
        :return: Temperature in Celsius
        """

        # 1. Read low level counter -> psutil -> sensors.
        try:
            cpu_temp = psutil.sensors_temperatures()

            if cpu_temp:
                core_temp = cpu_temp.get(self._CPU_SENSOR, [])
                for sensor in core_temp:
                    if (sensor.label == self._CPU_LABEL
                        and sensor.current is not None):
                        return float(sensor.current)

            all_valid_temps: list[float] = []
            for sensor_list in cpu_temp.values():
                for s in sensor_list:
                    if s.current is not None and s.current > 0:
                        all_valid_temps.append(s.current)

            if all_valid_temps:
                return max(all_valid_temps)
        except Exception:
            pass

        # 2. Read sysfs -> /sys/class/thermal/thermal_zone0/temp
        try:
            sys_temps: list[float] = []
            thermal_zones = Path("/sys/class/thermal").glob("thermal_zone*")

            for zone in thermal_zones:
                temp_file = zone / "temp"
                if temp_file.exists():
                    val = float(temp_file.read_text().strip())

                    if val > 1000:
                        val /= 1000.0
                    if 0 < val < 115:
                        sys_temps.append(val)

            if sys_temps:
                return max(sys_temps)
        except Exception:
            pass
        return 0.0


    def _read_bat_power(self) -> float:
        try:
            return float(Path(self._bat_file).read_text())
        except PermissionError:
            return 0.0
        except FileNotFoundError:
            return 0.0

    def _current_energy(self) -> None:
        bat_power_uw: float = self._read_bat_power()
        now: float = time.perf_counter()
        dt: float = now - self._last_time
        self._last_time = now

        if bat_power_uw != 0.0:
            estimated_power_w: float = bat_power_uw / self._uw_to_w
        else:
            load = self._process.cpu_percent(interval=0)
            estimated_power_w: float = 5.0 + (self._tdp - 5.0) * load
        self._acc_energy_j_cpu += estimated_power_w * dt


    # SETTER
    def reset_baseline(self) -> None:
        self._acc_energy_j_cpu = 0.0
        self._last_time = time.perf_counter()

    # GETTERS
    def get_cpu_load(self) -> float:
        return self._process.cpu_percent(interval=0)

    def get_cpu_freq(self) -> float:
        freq = psutil.cpu_freq()
        return freq.current if freq else 0.0

    def get_cpu_temp(self) -> float:
        return self._current_cpu_temperature()

    def get_cpu_energy(self) -> float:
        self._current_energy()
        return self._acc_energy_j_cpu

    def get_ram_rss(self) -> float:
        return self._process.memory_full_info().rss

    def get_ram_uss(self) -> float:
        return self._process.memory_full_info().uss


"""
+-------------------------------------------+
|Apple Silicon Telemetry:                   |
|1. Measurement RAM RSS.                    |
|2. Measurement RAM USS.                    |
|3. Measurement CPU LOAD.                   |
|4. Measurement CPU FREQ -> power-metrics.  |
|5. Measurement CPU TEMP -> power-metrics.  |
|6. Measurement CPU ENERGY -> power-metrics.|
+-------------------------------------------+
"""
class AppleSiliconTelemetry(BaseTelemetry):
    def __init__(self) -> None:
        self._process = psutil.Process(os.getpid())
        self._proc: subprocess.Popen | None = None
        self._warmup()

        # Started DEMON
        self._running: bool = True
        self._monitor_thread = threading.Thread(
            target=self._bg_powermetrics_reader,
            daemon=True
        )
        self._monitor_thread.start()

        # Buffer cache values telemetry
        self._acc_energy_j_cpu: float = 0.0
        self._current_freq_mhz_cpu: float = 0.0
        self._current_temperature_cpu: float = 0.0
        self._last_time: float = time.perf_counter()

        # CONSTS:
        self._mw_to_w: Final[float] = 1000.0
        self._ghz_to_mhz: Final[float] = 1000.0


    def __del__(self) -> None:
        self._running = False

        if self._proc:
            self._proc.terminate()

        if self._monitor_thread.is_alive():
            self._monitor_thread.join()


    def _warmup(self) -> None:
        self._process.cpu_percent(interval=3)


    def _bg_powermetrics_reader(self) -> None:
        cmd: list[str] = [
            "sudo",
            "powermetrics",
            "-i",
            "100",
            "-s",
            "cpu_power,thermal"
        ]
        self._proc = subprocess.Popen(
            cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True
        )

        buffer: list[str] = []
        for line in self._proc.stdout:
            if not self._running:
                break
            buffer.append(line)

            if line.startswith("***") and buffer:
                text: str = "".join(buffer)
                self._parse_stdout_low_level_counter(text)
                buffer.clear()

    def _parse_stdout_low_level_counter(self, text_cli: str) -> None:
        pattern_power: str = r"CPU Power:\s*([\d.]+)\s*(mW|W)"
        pattern_freq: str = r"(?:P-Cluster|CPU).*?frequency:\s*([\d.]+)\s*(MHz|GHz)"

        metrics_power = re.search(pattern_power, text_cli)
        metrics_freq = re.search(pattern_freq, text_cli)

        # BLOCK 1: Parse power -> energy:
        if metrics_power:
            now: float = time.perf_counter()
            dt: float = now - self._last_time
            value = float(metrics_power.group(1))
            unit = metrics_power.group(2)
            self._last_time = now

            if unit == "mW":
                self._acc_energy_j_cpu += (value / self._mw_to_w) * dt
            else:
                self._acc_energy_j_cpu += value * dt

        # BLOCK 2: Parse frequency:
        # P-Cluster (Performance) OR E-Cluster (Efficiency)
        if not metrics_freq:
            pattern_freq_e = r"E-Cluster.*?frequency:\s*([\d.]+)\s*(MHz|GHz)"
            metrics_freq = re.search(pattern_freq_e, text_cli)

        if not metrics_freq:
            self._current_freq_mhz_cpu = 0.0
        else:
            value = float(metrics_freq.group(1))
            unit = metrics_freq.group(2)

            if unit == "GHz":
                value *= self._ghz_to_mhz
            self._current_freq_mhz_cpu = value

        # BLOCK 3: Parse temperature:
        if "Nominal" in text_cli:
            self._current_temperature_cpu = 35.0
        elif "Fair" in text_cli:
            self._current_temperature_cpu = 55.0
        elif "Serious" in text_cli:
            self._current_temperature_cpu = 75.0
        elif "Critical" in text_cli:
            self._current_temperature_cpu = 95.0


    # SETTER
    def reset_baseline(self) -> None:
        self._acc_energy_j_cpu = 0.0
        self._last_time = time.perf_counter()

    # GETTERS
    def get_cpu_load(self) -> float:
        return self._process.cpu_percent(interval=0)

    def get_cpu_freq(self) -> float:
        return self._current_freq_mhz_cpu

    def get_cpu_temp(self) -> float:
        return self._current_temperature_cpu

    def get_cpu_energy(self) -> float:
        return self._acc_energy_j_cpu

    def get_ram_rss(self) -> float:
        return self._process.memory_full_info().rss

    def get_ram_uss(self) -> float:
        return self._process.memory_full_info().uss


"""
+-------------------------------------------------------+
|Telemetry Factor:                                      |
|1. MacOS -> Apple Silicon Telemetry.                   |
|2. Modern Intel{13-14} -> Modern Intel Linux Telemetry.|
|3. Legacy Intel{1-2} -> Legacy Intel Linux Telemetry.  |
+-------------------------------------------------------+
"""
class TelemetryFactor:
    @staticmethod
    def create_telemetry(arch_name: str) -> BaseTelemetry:
        if "apple" in arch_name or "darwin" in arch_name:
            return AppleSiliconTelemetry()
        elif "13500h" in arch_name or "14500h" in arch_name:
            return ModernIntelLinuxTelemetry()
        elif "750m" in arch_name or "x86_64" in arch_name:
            return LegacyIntelLinuxTelemetry()
        else:
            return ModernIntelLinuxTelemetry()


"""
+------------------------------+
|Profile:                      |
|1. max measurement RAM RSS.   |
|2. max measurement RAM USS.   |
|3. max measurement CPU LOAD.  |
|4. max measurement CPU FREQ.  |
|5. max measurement CPU TEMP.  |
|6. max measurement CPU ENERGY.|
+------------------------------+
"""
class Profiler:
    def __init__(self) -> None:
        self._config = Config()
        self._running: bool = False
        self._lock = threading.Lock()
        self.thread: threading.Thread | None = None
        self._arch_name: str = self._config.arch_name

        self._ram_rss: list[float] = []
        self._ram_uss: list[float] = []
        self._cpu_load: list[float] = []
        self._cpu_freq: list[float] = []
        self._cpu_temp: list[float] = []
        self._cpu_energy: list[float] = []

        # CONSTS: dt -> sleep, B_to_MB, CPU: sensor
        self._interval: Final[float] = 0.05
        self._B_TO_MB: Final[float] = 1024 * 1024

        # Model Telemetry
        self._telemetry: BaseTelemetry = TelemetryFactor.create_telemetry(
            self._arch_name.lower()
        )


    def _worker(self) -> None:
        while self._running:
            t_0 = time.perf_counter()

            # CPU: load, freq, temp, energy
            cpu_load = self._telemetry.get_cpu_load()
            cpu_temp = self._telemetry.get_cpu_temp()
            cpu_freq = self._telemetry.get_cpu_freq()
            cpu_energy = self._telemetry.get_cpu_energy()

            # RAM: rss, uss
            rss = self._telemetry.get_ram_rss()
            uss = self._telemetry.get_ram_uss()

            with self._lock:
                self._cpu_energy.append(cpu_energy)
                self._cpu_load.append(cpu_load)
                self._cpu_freq.append(cpu_freq)
                self._cpu_temp.append(cpu_temp)
                self._ram_rss.append(rss)
                self._ram_uss.append(uss)

            dt = time.perf_counter() - t_0
            sleep_time = max(0, self._interval - dt)
            time.sleep(sleep_time)


    def start_measure(self) -> None:
        self._telemetry.reset_baseline()

        with self._lock:
            self._ram_rss.clear()
            self._ram_uss.clear()
            self._cpu_load.clear()
            self._cpu_freq.clear()
            self._cpu_temp.clear()
            self._cpu_energy.clear()

        self._running = True
        self.thread = threading.Thread(
            target=self._worker,
            daemon=True
        )
        self.thread.start()

    def stop_measure(self) -> None:
        self._running = False
        self.thread.join()


    def _safe_max(self, list_exp: list[float],
                  flag_b_to_mb: bool=False) -> float:
        if list_exp:
            if flag_b_to_mb:
                return max(list_exp) / self._B_TO_MB
            else:
                return max(list_exp)
        else:
            return 0.0

    # GETTERS
    def get_max_cpu_load(self) -> float:
        with self._lock:
            return self._safe_max(self._cpu_load)

    def get_max_cpu_freq(self) -> float:
        with self._lock:
            return self._safe_max(self._cpu_freq)

    def get_max_cpu_temp(self) -> float:
        with self._lock:
            return self._safe_max(self._cpu_temp)

    def get_max_cpu_energy(self) -> float:
        with self._lock:
            return self._safe_max(self._cpu_energy)

    def get_max_ram_rss(self) -> float:
        with self._lock:
            return self._safe_max(self._ram_rss, True)

    def get_max_ram_uss(self) -> float:
        with self._lock:
            return self._safe_max(self._ram_uss, True)


"""
+-----------------------------------------------------+
|Model telemetry:                                     |
|1. Benchmark itr -> python eval generation equations.|
|2. Benchmark itr -> custom eval generation equations.|
|3. Save Data{MATRIX} python eval -> export data csv. |
|4. Save Data{MATRIX} custom eval -> export data csv. |
+-----------------------------------------------------+
"""
class ModelTelemetry:
    # Declaration arrays
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

    def __init__(self) -> None:
        tracemalloc.start(1)
        self.config = Config()
        self.profile = Profiler()
        self.max_eq: Final[int] = 30200
        self.dict_digits = DictDigits()
        self.config_eval = EquationConfig(self.max_eq)
        self.config_custom_eval = CustomConfig(self.max_eq)
        self.python_eval = EvalEquation(self.config_eval)
        self.custom_eval = CustomEval(self.config_custom_eval)

        # CONSTS: Size matrix
        self.rows: Final[int] = len(self.dict_digits.dict_digits_4)
        self.columns: Final[int] = len(self.dict_digits.dict_digits_4['4-generation-equation-1'])

        # Initialization
        # CPU DATA:
        self.matrix_cpu_load_eval = np.zeros((self.rows, self.columns), dtype=np.float64)
        self.matrix_cpu_freq_eval = np.zeros((self.rows, self.columns), dtype=np.float64)
        self.matrix_cpu_temp_eval = np.zeros((self.rows, self.columns), dtype=np.float64)
        self.matrix_cpu_energy_eval = np.zeros((self.rows, self.columns), dtype=np.float64)
        self.matrix_cpu_load_c_eval = np.zeros((self.rows, self.columns), dtype=np.float64)
        self.matrix_cpu_freq_c_eval = np.zeros((self.rows, self.columns), dtype=np.float64)
        self.matrix_cpu_temp_c_eval = np.zeros((self.rows, self.columns), dtype=np.float64)
        self.matrix_cpu_energy_c_eval = np.zeros((self.rows, self.columns), dtype=np.float64)

        # RAM DATA:
        self.matrix_ram_rss_eval = np.zeros((self.rows, self.columns), dtype=np.float64)
        self.matrix_ram_uss_eval = np.zeros((self.rows, self.columns), dtype=np.float64)
        self.matrix_py_heap_eval = np.zeros((self.rows, self.columns), dtype=np.float64)
        self.matrix_ram_rss_c_eval = np.zeros((self.rows, self.columns), dtype=np.float64)
        self.matrix_ram_uss_c_eval = np.zeros((self.rows, self.columns), dtype=np.float64)
        self.matrix_py_heap_c_eval = np.zeros((self.rows, self.columns), dtype=np.float64)


    def _forward_model(self, func_equation,
                       dict_matrix: dict[str, NDArray[np.float64]]) -> None:
        ITERATIONS: Final[int] = 10

        for i, (name, digits) in enumerate(self.dict_digits.dict_digits_4.items()):
            for j, digit in enumerate(digits):
                # Init state
                self.profile.start_measure()
                snap_before = tracemalloc.take_snapshot()

                # Func create equations
                for _ in range(ITERATIONS):
                    func_equation(digit)

                # Final state
                snap_after = tracemalloc.take_snapshot()
                self.profile.stop_measure()

                stats = snap_after.compare_to(snap_before, "lineno")
                total_alloc = sum(s.size_diff for s in stats if s.size_diff > 0)
                total_alloc /= 1024

                print("CPU load %:", self.profile.get_max_cpu_load())
                print("CPU freq:", self.profile.get_max_cpu_freq())
                print("CPU temp:", self.profile.get_max_cpu_temp())
                print("CPU energy: ", self.profile.get_max_cpu_energy())
                print("RAM RSS:", self.profile.get_max_ram_rss())
                print("RAM USS:", self.profile.get_max_ram_uss())
                print("RAM PY MEM:", total_alloc)

                dict_matrix["cpu_load"][i, j] = self.profile.get_max_cpu_load()
                dict_matrix["cpu_freq"][i, j] = self.profile.get_max_cpu_freq()
                dict_matrix["cpu_temp"][i, j] = self.profile.get_max_cpu_temp()
                dict_matrix["cpu_energy"][i, j] = self.profile.get_max_cpu_energy()
                dict_matrix["ram_rss"][i, j] = self.profile.get_max_ram_rss()
                dict_matrix["ram_uss"][i, j] = self.profile.get_max_ram_uss()
                dict_matrix["py_heap"][i, j] = total_alloc


    def _forward_telemetry(self) -> None:
        matrix_eval: dict[str, NDArray[np.float64]] = {
            "ram_rss": self.matrix_ram_rss_eval,
            "ram_uss": self.matrix_ram_uss_eval,
            "py_heap": self.matrix_py_heap_eval,
            "cpu_load": self.matrix_cpu_load_eval,
            "cpu_freq": self.matrix_cpu_freq_eval,
            "cpu_temp": self.matrix_cpu_temp_eval,
            "cpu_energy": self.matrix_cpu_energy_eval
        }
        matrix_c_eval: dict[str, NDArray[np.float64]] = {
            "ram_rss": self.matrix_ram_rss_c_eval,
            "ram_uss": self.matrix_ram_uss_c_eval,
            "py_heap": self.matrix_py_heap_c_eval,
            "cpu_load": self.matrix_cpu_load_c_eval,
            "cpu_freq": self.matrix_cpu_freq_c_eval,
            "cpu_temp": self.matrix_cpu_temp_c_eval,
            "cpu_energy": self.matrix_cpu_energy_c_eval
        }

        # BENCHMARKS: forward_model
        print("CUSTOM EVAL()")
        self._forward_model(self.custom_eval.process_equation_all_possible, matrix_c_eval)

        print("PYTHON EVAL()")
        self._forward_model(self.python_eval.process_equation_all_possible, matrix_eval)


    def _export_data(self) -> None:
        results: dict[str, NDArray[np.float64]] = {
            **{
                self.config.file_cpu_load_ev: self.matrix_cpu_load_eval,
                self.config.file_cpu_freq_ev: self.matrix_cpu_freq_eval,
                self.config.file_cpu_temp_ev: self.matrix_cpu_temp_eval,
                self.config.file_ram_rss_ev: self.matrix_ram_rss_eval,
                self.config.file_ram_uss_ev: self.matrix_ram_uss_eval,
                self.config.file_py_heap_ev: self.matrix_py_heap_eval,
                self.config.file_cpu_energy_ev: self.matrix_cpu_energy_eval
            },
            **{
                self.config.file_cpu_load_c_ev: self.matrix_cpu_load_c_eval,
                self.config.file_cpu_freq_c_ev: self.matrix_cpu_freq_c_eval,
                self.config.file_cpu_temp_c_ev: self.matrix_cpu_temp_c_eval,
                self.config.file_ram_rss_c_ev: self.matrix_ram_rss_c_eval,
                self.config.file_ram_uss_c_ev: self.matrix_ram_uss_c_eval,
                self.config.file_py_heap_c_ev: self.matrix_py_heap_c_eval,
                self.config.file_cpu_energy_c_ev: self.matrix_cpu_energy_c_eval
            }
        }

        for file, matrix in results.items():
            np.savetxt(file, matrix, delimiter=",", fmt="%.6f")


    def run_model(self) -> None:
        self._forward_telemetry()
        self._export_data()


if __name__ == "__main__":
    telemetry = ModelTelemetry()
    telemetry.run_model()
