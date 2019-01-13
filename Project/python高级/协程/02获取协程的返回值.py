
#获取协程的返回值
import asyncio
import time
async  def get_html(url):
    print("start get url")
    await asyncio.sleep(2)
    # print("start get url")
    return "chenze"


#如果要在callback函数中传递多个参数的话，要使用寿命方法去解决呢？
# 可以使用偏函数
from functools import partial
def callback(url,furure):
    print(url)
    print("send email to chenze")



if __name__ == '__main__':
    start_time = time.time()
    loop = asyncio.get_event_loop()
    # asyncio.ensure_future() 通过此方法拿到一个future对象
    # 为啥loop不提供一个方法呢?而是用这个asyncio.ensure_future()呢？
    # 其实loop也是有一个方法的，loop.create_task()
    # 这两个方法是等效的，差别不是很大
    get_furure = asyncio.ensure_future(get_html("www.baidu.com"))
    # tasks = [get_html("www.baidu.com") for i in range(10)]
    # loop.run_until_complete(asyncio.wait(tasks))


    # get_furure.add_done_callback(callback)
    get_furure.add_done_callback(partial(callback,"www.baidu.com"))

    # run_until_complete()接收参数的类型比较丰富
    loop.run_until_complete(get_furure)
    print(get_furure.result())






























