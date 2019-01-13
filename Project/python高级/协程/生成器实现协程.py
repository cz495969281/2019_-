

"""
生成器实现协程
我们希望协程是用单线程进行调度的，这时我就不需要像线程一样让操作系统去调度,协程是由程序员自己去调度的
它没有深入到内核级别去调度，线程和进程都是内核级别的一个调度，协程实际是函数级别的调度，是程序员自己去
调度的，协程可以像编写同步代码一样去编写异步代码

生成器就可以完成协程的功能
生成器是可以暂停的函数，它是有状态的
"""

"""
python一切皆对象，栈帧对象，字节码对象
函数调用的最大的特点就是：栈帧都是分配的在内存上，这就决定了栈帧可以独立于调用者存在；所以这是
生成器实现的可能
"""
import inspect
def gen_func():

    """
    value = yield 1
    两层含义:
    第一  返回值给调用方
    第二  调用方通过send方式返回给gen
    """
    value = yield 1
    return "chenze"

if __name__ == '__main__':
    gen = gen_func()

    #下面这个方法可以查询到生成器的状态是什么
    print(inspect.getgeneratorstate(gen))   #  GEN_CREATED
    next(gen)
    print(inspect.getgeneratorstate(gen))    # GEN_SUSPENDED 暂停的状态

    try:
        next(gen)
    except StopIteration as e:
        pass
    print(inspect.getgeneratorstate(gen))   #GEN_CLOSED




"""
协程的调度依然是   事件循环 + 协程模式(协程是单线程模式)
遇到消耗IO的操作  一定要去调用yield 或者yield from 
"""





























