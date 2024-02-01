import os

from .measurements import MeasurementProxy
from .minifier import MinificationStrategyFactory, Minifier


class FileManager:
    def __init__(self, file):
        self.file = file
        self.size = 0
        self.format = ""
        self.memory_usage = 0
        self.duration = 0

    def set_file_size(self, size):
        self.size = size

    def set_file_format(self, format):
        self.format = format

    def set_file_minify_memory_usage(self, usage):
        self.memory_usage = usage

    def set_file_minify_duration_time(self, time):
        self.duration = time

    def get_file_size(self):
        file_size_kb = self.size / 1024
        return f"{file_size_kb:.2f} KB"

    def get_file_format(self):
        return self.format

    def get_file_minify_memory_usage(self):
        return f"{self.memory_usage:.2f} B"

    def get_file_minify_duration(self):
        duration_milisec = self.duration * 1000
        return f"{duration_milisec:.6f} ms"

    def save_minify(self, file_path, strategy):
        strategy_factory = MinificationStrategyFactory()
        strategy = strategy_factory.create_strategy(strategy)
        minification_proxy = MeasurementProxy(strategy)
        minifier = Minifier(minification_proxy)
        file_size, memory_usage, spent_time = minifier.minify_file(self.file, file_path)
        self.set_file_size(file_size)
        self.set_file_minify_memory_usage(memory_usage)
        self.set_file_minify_duration_time(spent_time)

    def save_file(self, file_path, minify):
        file_format = os.path.splitext(self.file.filename)[1]
        self.set_file_format(file_format)
        strategy = None
        if file_format.lower() == ".css":
            strategy = "css"
        elif file_format.lower() == ".js":
            strategy = "js"
        elif file_format.lower() in [
            ".jpeg",
            ".png",
            ".gif",
            ".bmp",
            ".tiff",
            ".svg",
            ".ico",
        ]:
            strategy = "img"
        if not strategy and minify:
            raise ValueError("Format not supported")
        if minify:
            self.save_minify(file_path=file_path, strategy=strategy)
        else:
            with open(file_path, "wb") as output_file:
                output_file.write(self.file.file.read())
            file_size = os.path.getsize(file_path)
            self.set_file_size(file_size)
