from abstracts import MinificationStrategy
from measurements import MeasurementProxy
import magic


# Concrete strategies
class CssMinificationStrategy(MinificationStrategy):
    def minify(self, content):
        return content.replace(" ", "").replace("\n", "")


class JsMinificationStrategy(MinificationStrategy):
    def minify(self, content):
        return content.replace(" ", "").replace("\n", "").replace("\t", "")


class Minifier:
    def __init__(self, minification_strategy):
        self.minification_strategy = minification_strategy

    def set_strategy(self, minification_strategy):
        self.minification_strategy = minification_strategy

    def minify_file(self, file_path):
        with open(file_path, "r") as file:
            content = file.read()
            minified_content = self.minification_strategy.minify(content)
            # Save the minified content back to the file
            with open(file_path, "w") as output_file:
                output_file.write(minified_content)


# Creational: Factory Method pattern
class MinificationStrategyFactory:
    def create_strategy(self, strategy_type):
        if strategy_type == "css":
            return CssMinificationStrategy()
        elif strategy_type == "js":
            return JsMinificationStrategy()
        else:
            raise ValueError("Invalid strategy type")


class FileMinifier:
    def __init__(self, file_name, measure_callback):
        self.file_name = file_name
        self.measure_callback = measure_callback

    def minify_file(self, file_path):
        strategy_factory = MinificationStrategyFactory()
        mime = magic.Magic()
        file_format = mime.from_file(file_path)
        if file_format not in ["css", "js"]:
            raise ValueError("Format not supported")
        strategy = strategy_factory.create_strategy(file_format)
        strategy_proxy = MeasurementProxy(strategy, self.measure_callback)
        minifier = Minifier(strategy_proxy)
        minifier.minify_file(file_path)
