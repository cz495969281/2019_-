#1.run_until_completa  #理解为多线程编程中的join方法
# import asyncio
# loop = asyncio.get_event_loop()
# loop.run_forever()
#因为在之前介绍回调和事件循环，我们看到当时的loop是处于一个不断的循环，并不会停止

#它在我们运行了指定的协程之后，它会停止掉，run_forever()是不会停止的，会一直执行下去
# 那么run_until_complete()是怎么做到在运行完一个协程之后立即停止掉的
# asyncio源码包的base_events文件中 future.add_done_callback(_run_until_complete_cb)这个方法执行完后
# 会去执行_run_until_complete_cb()方法，这个方法会将事件循环停止掉
# 而run_until_complete()也会去执行run_forever(),run_until_complete()是将制定的future执行完后停止掉
# loop.run_until_complete()


# asyncio的弊端：
#loop会被方法future里面，在任何一个future里面获取task中，loop都可以被停止掉
# 整个asyncio的逻辑是比较混乱的，看过源码可以得知，整个loop放入future中，整个future
# 放入到loop中，凑成了一种环状，很容易引起循环引用的


# 如何去取消future(task)?
# 案例：
#     比如现在正在做一个数据的采集入库，因为采集的数据量特别大，一次性采集的数据可以要入很多张表，
#     入库过程可能会比较慢，这样的话，在某一张表失败的时候或者是某一张表发出信号，就可以判断整个入库
#     有失败的，就需要将其他入库的请求取消掉

import asyncio
import time

async def get_html(sleep_times):
    print("waiting")
    await asyncio.sleep(sleep_times)

    print("done after {}s".format(sleep_times))


if __name__ == '__main__':
    task1 = get_html(1)
    task2 = get_html(2)
    task3 = get_html(3)
    tasks = [task1,task2,task3]
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(asyncio.wait(tasks))
    except KeyboardInterrupt as e:
        all_tasks= asyncio.Task.all_tasks()
        for task in all_tasks:
            print("cancal task")
            print(task.cancel())

        loop.stop()
        # 后面一定要跟上 loop.run_forever()，不写的话是会报异常的
        loop.run_forever()
    finally:
        loop.close()
