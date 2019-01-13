
# async def downloader(url):
#     return "chenze"


from collections import Awaitable
#async后面跟着是一个Awaitable对象

import types
@types.coroutine
def downloader(url):
    yield "chenze"

async def download_url(url):
    #dosomething
    #await 可以理解为 yield from
    html = await downloader(url)
    return html


if __name__ == '__main__':
    coro = download_url("www.baidu.com")
    # next(None) 原生的协程不能用next()进行调用
    coro.send(None)
