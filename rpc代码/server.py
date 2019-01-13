from services import InvalidOperation
from services import Server


class Handlers:

    @staticmethod
    def divide(num1, num2=1):
        """
        除法
        :param num1: int
        :param num2: int
        :return: float
        """
        if num2 == 0:
            raise InvalidOperation('itcast')
        val = num1 / num2
        return val


if __name__ == '__main__':
    # 开启服务器
    _server = Server('127.0.0.1', 8000, Handlers)
    _server.serve()