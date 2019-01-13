# 什么是迭代协议
# 迭代器是什么 ？  迭代器是访问集合内元素的一种方式，一般用来遍历数据
# 迭代器和以下标的访问方式不一样，迭代器是不能返回的，迭代器提供了一种惰性方式数据的方式

# 迭代协议 实际上就是  可迭代类型和Iterator
# __iter__返回的是一个可迭代对象

from collections.abc import Iterator,Iterable
# Iterator  __iter__  __next__（核心） 实现这两个方法是一个迭代器

from collections import UserList