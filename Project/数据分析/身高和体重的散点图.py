# import matplotlib.pyplot as plt
#
#
# height = [161,170,182,175,173,165]
# weight = [50,58,80,70,69,55]
#
# plt.scatter(height,weight)
# plt.show()

"""
散点图最大的特性就是研究两个变量的相关性

相关性一般有三种情况：正相关、负相关、不相关
"""

# A0 = (i for i in range(10) if i % 2 ==0)
# A1 = {i:i+2 for i in A0}
# A2 = sorted(A0,reverse=True)
# print(A0)
# print(A1)
# print(A2)
def decorate(func):
    print("func")
    def inner(**kwargs):
        kwargs.update(a='b')
        result = func(**kwargs)
        return result
    print('inner')
    return inner

@decorate
def func(**kwargs):
    return kwargs
print(func(a='c'))