import os
from app.services.base import MinificationStrategy
from PIL import Image
from io import BytesIO

# Concrete strategies
class CssMinificationStrategy(MinificationStrategy):
    def minify(self, content):
        content = content.decode()
        return content.replace(" ", "").replace("\n", "").encode()


class JsMinificationStrategy(MinificationStrategy):
    def minify(self, content):
        content = content.decode()
        return content.replace(" ", "").replace("\n", "").replace("\t", "").encode()


class ImgMinificationStrategy(MinificationStrategy):
    def minify(self, content):
        quality = 80
        with Image.open(BytesIO(content)) as img:
            webp_bytesio = BytesIO()
            img.save(webp_bytesio, "WEBP", quality=quality)
            webp_bytes = webp_bytesio.getvalue()

        return webp_bytes


# Creational: Factory Method pattern
class MinificationStrategyFactory:
    def create_strategy(self, strategy_type):
        if strategy_type == "css":
            return CssMinificationStrategy()
        elif strategy_type == "js":
            return JsMinificationStrategy()
        elif strategy_type == "img":
            return ImgMinificationStrategy()
        else:
            raise ValueError("Invalid strategy type")


class Minifier:
    def __init__(self, minification_proxy):
        self.minification_proxy = minification_proxy

    def minify_file(self, file, file_path):
        file.file.seek(0)
        content = file.file.read()
        content, memory_usage, spent_time = self.minification_proxy.minify(content)
        with open(file_path, "wb") as output_file:
            output_file.write(content)
        file_size = os.path.getsize(file_path)
        return file_size, memory_usage, spent_time
