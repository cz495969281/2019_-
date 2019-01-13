#类也是对象，type创建类的类
def create_class(name):
    if name == "user":
        class User:
            def __str__(self):
                return "user"
        return User

    elif name == "company":
        class Company:
            def __str__(self):
                return "company"

        return Company


#type动态创建类
# User = type("User",(),{})

def say(self):
    return "i am name"


class BaseClass:
    def answer(self):
        return "i am baseclass"


#什么是元类，元类是创建类的类  对象<--class(对象) <-type

class MetaClass(type):
    pass

class Model(metaclass=MetaClass):
    pass

#python中类的实例化过程，会首先寻找metaclass这个属性，会通过
# metaclass去创建Model类


if __name__ == "__main__":
    # MyClass = create_class("user")
    # my_obj = MyClass()
    # print(my_obj)

    # User = type("User", (), {})
    # User = type("User", (), {"name":"cz","say":say})
    # my_obj = User()
    # print(my_obj.name)
    # print(my_obj.say())

    User = type("User",(BaseClass,),{"name":"cz","say":say})
    my_obj = User()
    print(my_obj.answer())

