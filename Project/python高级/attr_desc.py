#类如何变成属性描述符,我们只需要去实现 __get__ 方法 或者 __set__
# 以及__delete__三者中的任何一个方法都是属性描述符

import numbers

class IntField(object):
    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if not isinstance(value,numbers.Integral):
            raise ValueError("int value need")

        if value < 0:
            raise ValueError("position value need")

        self.value = value

    def __delete__(self, instance):
        pass



class NonDataInField:
    #非数据属性描述符
    def __get__(self, instance, owner):
        return self.value






#属性描述符可以做什么呢？
#age只要实现上述类中的任何一个魔法方法就是一个属性描述符对象
class User:
    age = IntField()



"""
如果user是某个类的实例，那么user.age(以及等价的getattr(user,"age"))
首先调用__getattribute__。如果类定义了__getattr__方法，
那么在__getattribute__抛出AttributeError的时候就会调用到__getattr__
而对于描述符(__get__)的时候，则是发生在__getattribute__内部
user = User(),那么user.age 顺序如下：
（1）如果“age”是出现在User或其基类的__dict__中， 且age是data descriptor， 那么调用其__get__方法, 否则

（2）如果“age”出现在user的__dict__中， 那么直接返回 obj.__dict__[‘age’]， 否则

（3）如果“age”出现在User或其基类的__dict__中

（3.1）如果age是non-data descriptor，那么调用其__get__方法， 否则

（3.2）返回 __dict__[‘age’]

（4）如果User有__getattr__方法，调用__getattr__方法，否则

（5）抛出AttributeError"""

if __name__ == "__main__":
    user = User()
    #这里对age进行赋值的时候其实就是调用了InField类中的__set__方法
    user.__dict__["age"] = "abc"
    # print(user.__dict__)
    print(user.age)
    pass