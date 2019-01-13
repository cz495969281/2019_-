# name_list = ["bobby1","bobby2"]
# name_list = ("bobby1","bobby2")
# for name in name_list:
#     print(name)

from collections import namedtuple

############################################
# class User:
#     def __init__(self,name,age,height):
#         self.name = name
#         self.age = age
#         self.height = height
#
# user = User(name="cz",age=25)
# print(user.name,user.age)
############################################


#可以用namedtuple生成一个类，它不是一个对象
#namedtuple是tuple的一个子类，它相对于上述User类来说，首先代码简单，然后namedtuple是很省空间的，省去了class类中
#很多的内置变量，在内存和效率上都是非常高的，它在创建一些简单的对象的时候是非常适用的

User = namedtuple("user",["name","age","height","edu"])
user_tuple = ("cz",18,190)
user_list = ["cz",18,190,"master"]
# user_dict = {
#     "name":"cz",
#     "age":15,
#     "height":175
# }
# user = User(name="cz",age=25,height=170)
# user = User(*user_tuple,"master")

# user = User(**user_dict,edu="master")
# user = User._make(user_list) #用_make方法就不需要考虑传递参数的时候*或者**的问题，只需要传递是一个可迭代对象

user = User("cz",25,170,"master")
# print(type(user)
name,age,*other = user
user_info_dict = user._asdict()  #_asdict() 把字典变成一个Orderdict类型
print(user.age,user.name,user.height)