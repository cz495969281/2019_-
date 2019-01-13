# 事件循环 + 回调(驱动生成器) + epoll(IO多路复用)
#asyncio是python用于解决异步IO编程的一整套解决方案
#tornado、gevent 、twisted(scrapy,django_channels)
# tornado实现了web服务器

# python webk框架中最流行的应该是django+flask，这两种是传统的阻塞IO的编程模型，
# django和flask是web系统开发框架，本身是不提供web服务器的(本身是不会去完成socket编码的)
# django和flask部署的时候，是不会用到他们的本身提供的运行机制的，它的运行机制是简单的实行了简单
# 的socket,它只是方便了我们的调试，真正部署的时候会搭配第三方实现socket的一些框架，比如uwsigi,gunicorn+nginx
# 搭配部署我们的web系统

# tornado可以直接部署，就是直接去启动tornado,它的一个并发问题我们都不用去管，它自己会去实现，它会去使用epoll
# 去连接一些socket请求，但是真正部署的时候还会去搭配nginx+tornado,nginx本身提供了很多功能，是tornado
# 提供不了的，比如说ip限制，log服务，静态文件代理等

#  在tornado中不能使用传统的pymysql的，比如说mysqlclient是不行的，或者说，它是达不到我们的一种并发
# 的效果的,原因就在这，pymysql和mysqlclient的接口都是阻塞的，我们的协程模式他是单线程的，所以在协程做数据
# 库驱动或者网络驱动的时候，一定要有一个异步库去实现我们对应的功能


import time
# time.sleep()  time.sleep()是同步阻塞，不能使用在async中
# 为什么协程中不建议使用time.sleep()呢?
# 首先，asyncio.sleep(2)是不管有同时执行10个任务还是1000个任务都会在2秒执行完成
# 然后time.time(2)的话，是不管执行2个任务还是1000个任务，而是每两秒执行一个任务，如果执行10个任务的话
# 就需要去20秒完成，1000个任务的话就需要2000秒完成

# 之所以会发生这种现象就是因为事件循环的原理，事件循环的原理，像select中的事件循环机制，在不停的调度函数
# 并且执行，它是一种单线程的模式，所有的逻辑都运行在事件循环里面
#
# time.sleep()是一种同步的操作 ，asyncio.sleep(2)是一种异步的操作

import asyncio
async def get_html(url):
    print("start get url")
    await asyncio.sleep(2)  #加上await等待这步执行完成后才会往下执行
    print("end get url")

if __name__ == '__main__':
    start_time = time.time()
    # asyncio.get_event_loop() 实现了事件循环，它会去完成之前说过的，类似于select这样的操作
    loop = asyncio.get_event_loop()


    tasks = [get_html("www.baidu.com") for i in range(10000)]



    #阻塞的方法，将协程放进去;  可以把这块理解之前多线程编程中的join方法
    # 会等到下面get_html这个协程执行完后才会去执行time.time()-start_time
    #1. loop.run_until_complete(get_html("www.baidu.com"))

    # asyncio.wait() 这里可以接收一个可迭代对象，等待这里所有的任务执行完之后才会去执行下一步
    loop.run_until_complete(asyncio.wait(tasks))

    print(time.time()-start_time)

# 我们可以把asyncio理解为协程池









































