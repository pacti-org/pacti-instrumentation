from typing import Iterator

def get_cpu_usage(cpu_measurement_interval: float) -> float: ...
def cpu_usage_plot(max_data_points: int = ..., finally_clear_output: bool = ..., cpu_measurement_interval: float = ...) -> Iterator: ...
