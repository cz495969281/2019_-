def ask(name="cz"):
    print(name)
"""
如果一个函数没有返回值的话，默认是返回一个None值的
"""

"""
1.赋值给一个变量
2.可以添加到集合对象中
3.可以作为参数传递给函数
4.可以当做函数的返回值

"""

class Person:
    def __init__(self):
        print("cz1")


obj_list = []
obj_list.append(ask)
obj_list.append(Person)

for item in obj_list:
    print(item())

#
# my_func = ask
# my_func("gq")
#
# my_class = Person
# my_class()