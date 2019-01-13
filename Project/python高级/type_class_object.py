a = 1
print(type(1))
print(type(int))

#type --> int --> 1
#type --> class --> obj

b= "abc"
print(type(b))
print(type(str))

"""
类是type这个类生成的一个对象，type也是一个类，同时type也是一个对象
我们平常所熟悉对象是由类对象来创建的  
object是所有类的顶层(基类)，必须继承它


object是type的实例，type也是自身的一个实例,type继承了object
"""