from abc import ABC, abstractmethod
import json

# ============================================================
# 1. Formatter：格式化器的抽象接口
# ============================================================
#
# Formatter 不负责打印日志。
# 它只规定一件事：
#
#     输入一个字符串 message
#     返回一个格式化之后的字符串
#
# 具体到底格式化成普通文本还是 JSON，
# Formatter 本身并不知道，而是交给子类决定。

class Formatter(ABC):

    @abstractmethod
    def format(self, message: str) -> str:
        pass

class PlainFormatter(Formatter):

    def format(self, message: str) -> str:
        return message

class JsonFormatter(Formatter):

    def format(self, message: str) -> str:
        log_data = {
            "log" : message
        }

        return json.dumps(log_data, ensure_ascii=False)

class Logger:
    
    def __init__(self, formatter: Formatter):
        # 保存外部传入的格式化器对象
        #
        # 这里并没有在 Logger 内部写死：
        #
        # self._formatter = PlainFormatter()
        #
        # 而是由外部决定使用哪一种 Formatter。
        #
        # 这种做法叫作“依赖注入”。
        self._formatter = formatter

    def log(self, message) -> None:
        formatted_message = self._formatter.format(message)

        print(formatted_message)

    

if __name__ == "__main__":
    plain_logger = Logger(PlainFormatter())
    plain_logger.log("Server started on port 8080")

    json_logger = Logger(JsonFormatter())
    json_logger.log("Server started on port 8080")