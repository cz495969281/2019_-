import asyncio

def callback(sleep_times):
    print("sleep {} success".format(sleep_times))


def stop_loop(loop):
    #将当前的loop停止掉，在适当的时候调用stop_loop()
    loop.stop()



if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    # 1.  call_soon()立即执行，并不代表下一行代码就执行，而是说在队列中等待一次循环的时候立马执行
    # loop.call_soon(callback,2)
    #
    # loop.call_soon(stop_loop,loop)


    #2.  call_later()根据我们延迟调用的时间，来确定他的一个先后顺序
    # loop.call_later(2,callback,2)
    # loop.call_later(1,callback,1)
    # loop.call_later(3,callback,3)

    #call_soon()比call_later()快，要先打印call_soon()
    # loop.call_soon(callback, 4)

    # 3 call_at指定的时间去运行回调函数，这个时间不是我们传统意义上的时间，而是loop里面的单调时间
    now = loop.time()
    loop.call_at(now+2,callback,2)
    loop.call_at(now+1,callback,1)
    loop.call_at(now+3,callback,3)
    loop.call_soon(callback, 4)

    #启动这个循环
    loop.run_forever()