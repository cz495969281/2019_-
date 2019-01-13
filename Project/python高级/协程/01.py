# 遇到的问题：
#     1.回调模式编码复杂度高
#     2.同步编程的并发性不高
#     3.多线程编程需要线程间同步，lock（锁会降低并发性能）

# 解决这些问题的方案
from  itertools import chain

my_list = [1,2,3]
my_dict = {
    "bobby1":"www.baidu.com",
    "bobby2":"www.qq.com"
}


#yield from iterable :将args中的可迭代对象中的值一个一个遍历出来
# def my_chain(*args,**kwargs):
#     for my_iterable in args:
#         yield from my_iterable
#         # for value in my_iterable:
#         #     yield value
#
# for value in my_chain(my_list,my_dict,range(5,10)):
#     print(value)

###############################################################

# def g1(iterable):
#     yield iterable
#
# def g2(iterable):
#     yield from iterable
#
# for value in g1(range(10)):
#     # 会将传递的进去对象直接打印出来
#     print(value)
#
# for value in g2(range(10)):
#     print(value)

####################################################
# def g1(gen):
#     yield from gen
#
# def main():
#     g = g1()
#     g.send(None)

# 1. main 调用方g1(委托生成器)gen子生成器
# 2.yield from 会在调用方与子生成器之间建立一个双向通道
def f(i,values=[]):
    values.append(i)
    return values


f(1)
print(f(2))
v=f(3)
print(v)
