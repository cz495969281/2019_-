# 服务器

#### 改写服务器程序，增加注册到zookeeper

```python
import threading
from kazoo.client import KazooClient

class ThreadServer(object):
    def __init__(self, host, port, handlers):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.host = host
        self.port = port
        self.sock.bind((host, port))
        self.handlers = handlers

    def serve(self):
        """
        开始服务
        """
        self.sock.listen(128)
        self.register_zk()
        print("开始监听")
        while True:
            conn, addr = self.sock.accept()
            print("建立链接%s" % str(addr))
            t = threading.Thread(target=self.handle, args=(conn,))
            t.start()
            
    def handle(self, client):
        stub = ServerStub(client, self.handlers)
        try:
            while True:
                stub.process()
        except EOFError:
            print("客户端关闭连接")
        
        client.close()
        
    def register_zk(self):
        """
        注册到zookeeper
        """
        self.zk = KazooClient(hosts='127.0.0.1:2181')
        self.zk.start()
        self.zk.ensure_path('/rpc')  # 创建根节点
        value = json.dumps({'host': self.host, 'port': self.port)
        # 创建服务子节点
        self.zk.create('/rpc/server', value.encode(), ephemeral=True, sequence=True)
```

#### 改写server.py，支持灵活启动服务器

```python
from services import ThreadServer
from services import InvalidOperation
import sys


class Handlers:
    @staticmethod
    def divide(num1, num2=1):
        """
        除法
        :param num1:
        :param num2:
        :return:
        """
        if num2 == 0:
            raise InvalidOperation()
        val = num1 / num2
        return val


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("usage:python server.py [host] [port]")
        exit(1)
    host = sys.argv[1]
    port = sys.argv[2]
    server = ThreadServer(host, int(port), Handlers)
    server.serve()
```

