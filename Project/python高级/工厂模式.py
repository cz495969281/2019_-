class Burger():
    name = ""
    price = 0.0

    def getPrice(self):
        return self.price

    def setPrice(self,price):
        self.price = price

    def getName(self):
        return self.name



class cheeseBurger(Burger):
    def __init__(self):
        self.name = "cheese burger"
        self.price = 10.0


class spicyChickenBurger(Burger):
    def __init__(self):
        self.name = "spicy chicken burger"
        self.price = 15.0



#小食
class Snack():
    name = ""
    price = 0.0
    type = "SNACK"
    def getPrice(self):
        return self.price

    def setPrice(self,price):
        self.price = price

    def getName(self):
        return self.name


class chips(Snack):
    def __init__(self):
        self.name = "chips"
        self.price = 6.0


class chickenWings(Snack):
    def __init__(self):
        self.name = "chicken wings"
        self.price = 12.0



#饮料
class Beverage():
    name = ""
    price = 0.0
    type = "BEVERAGE"

    def getPrice(self):
        return self.price

    def setPrice(self,price):
        self.price = price

    def getName(self):
        return self.name

class coke(Beverage):
    def __init__(self):
        self.name = "coke"
        self.price = 4.0


class milk(Beverage):
    def __init__(self):
        self.name = "milk"
        self.price = 5.0

#工厂模式
##################################3
"""
class foodFactory():
    type = ""
    def createFood(self,foodClass):
        print(self.type,"factory produce a instance")
        foodIns = foodClass()
        return foodIns


class burgerFactory(foodFactory):
    def __init__(self):
        self.type = "BURGER"

class snackFactory(foodFactory):
    def __init__(self):
        self.type="SNACK"
class beverageFactory(foodFactory):
    def __init__(self):
        self.type="BEVERAGE"
"""


# if __name__ == "__main__":
    # burger_factory = burgerFactory()
    # snack_factory = snackFactory()
    # beverage_factory = beverageFactory()

    # cheese_burger = beverage_factory.createFood(cheeseBurger)
    # print(cheese_burger.getName(),cheese_burger.getPrice())
    #
    # chicken_wings = snack_factory.createFood(chickenWings)
    # print(chicken_wings.getName(),chicken_wings.getPrice())
    #
    # coke_drink=beverage_factory.createFood(coke)
    # print(coke_drink.getName(),coke_drink.getPrice())


"""
工厂模式的定义如下：定义一个用于创建对象的接口，让子类决定实例化哪个类。
工厂方法使一个类的实例化延迟到其子类。其通用类图如下。
其产品类定义产品的公共属性和接口，工厂类定义产品实例化的“方式”。
"""
############################################################33


#简单工厂模式
# 这样，省去了将工厂实例化的过程。这种模式就叫做简单工厂模式。

class simpleFoodFactory():
    @classmethod
    def createFood(cls,foodClass):
        print("Simple factory produce a instance.")
        foodIns = foodClass()
        return foodIns

spicy_chicken_burger = simpleFoodFactory.createFood(spicyChickenBurger)
print(spicy_chicken_burger.name)


"""
工厂模式的优点：
    1.工厂模式巨有非常好的封装性，代码结构清晰；在抽象工厂模式中
其结构还可以随着需要进行，更深或者更浅的抽象层级调整，非常灵活
    2.屏蔽产品类，使产品的被使用业务场景和产品的功能细节可以分而开发进行
是比较典型的解耦框架。


工厂模式、抽象工厂模式的使用场景：
    1、当系统实例要求比较灵活和可扩展时，可以考虑工厂模式或者抽象工厂模式实现。比如
在通信系统中，高层通信协议会很多样化，同时，上层协议依赖于下层协议，那么就可以对应建
立对应层级的抽象工厂，根据不同的“产品需求”去生产定制的实例。


工厂类模式的不足：
1、工厂模式相对于直接生成实例过程要复杂一些，所以，在小项目中，可以不使用工厂模式；
2、抽象工厂模式中，产品类的扩展比较麻烦。毕竟，每一个工厂对应每一类产品，产品扩展，就意味着相应的抽象工厂也要扩展。


"""