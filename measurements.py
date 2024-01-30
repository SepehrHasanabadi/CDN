import time
import psutil
from abstracts import MinificationStrategy


# Decorator for measuring time
class TimeMeasurement(MinificationStrategy):
    def __init__(self, real_strategy):
        self._real_strategy = real_strategy

    def minify(self, content):
        start_time = time.time()
        result = self._real_strategy.minify(content)
        end_time = time.time()
        return result, end_time - start_time


# Decorator for measuring CPU usage
class MemoryMeasurement(MinificationStrategy):
    def __init__(self, real_strategy):
        self._real_strategy = real_strategy

    def minify(self, content):
        process = psutil.Process()
        memory_before = process.memory_info().rss
        result = self._real_strategy.minify(content)
        memory_after = process.memory_info().rss
        memory_usage = memory_after - memory_before
        return result, memory_usage


# Structural: Proxy pattern
class MeasurementProxy(MinificationStrategy):
    def __init__(self, real_strategy, measure_callback):
        self.measure_callback = measure_callback
        self._time_proxy = TimeMeasurement(real_strategy)
        self._ram_proxy = MemoryMeasurement(real_strategy)

    def minify(self, content):
        # Run both time and CPU measurements
        ram_result, memory_usage = self._ram_proxy.minify(content)
        result, spent_time = self._time_proxy.minify(ram_result)
        
        ram_usage_value = f"{memory_usage / (1024 * 1024):.2f} MB"
        spent_time_value = f"{spent_time:.6f}"
        if self.measure_callback:
            self.measure_callback(ram_usage_value, spent_time_value)

        return result
