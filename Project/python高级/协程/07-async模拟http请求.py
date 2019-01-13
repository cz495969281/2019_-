# asyncio 没有提供http协议的接口
# http协议请求url，可以使用aiohttp, aiohttp首先可以搭建一个http服务器，也可以做爬虫来使用，
# 当做异步的requests也是ok的
#
# aiohttp是基于async来完成的


import socket
from urllib.parse import urlparse


async def get_url(url):
    #通过socket请求html
    url = urlparse(url)
    host = url.netloc
    path = url.path
    if path == "":
        path = "/"

    #建立socket连接


    #不停的询问连接是否建立好， 需要while循环不停的去检查状态
    #做计算任务或者再次发起其他的连接请求

    client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode("utf8"))

    data = b""
    while True:
        d = client.recv(1024)
        if d:
            data += d
        else:
            break

    data = data.decode("utf8")
    html_data = data.split("\r\n\r\n")[1]
    print(html_data)
    client.close()