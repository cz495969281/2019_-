import matplotlib.pyplot as plt

plt.plot([1,2,3],[3,2,1])
plt.show()


#############
# Numpy是什么？
# 1.Numpy是python的开源的数值计算扩展
# 2.可用来存储和出来大型矩阵，比如python自身数据结构要高效
# 3.Numpy将Python变成一种免费的强大的Matlab系统

# ndarray
#   创建，一般有三种创建方式
#     1.从python的基础数据对象转化
#         """
#         import numpy as np
#         a = [1,2,3,4]
#         x1 = np.array(a)
#         type(x1)  #numpy.ndarray
#         """
#     2.通过Numpy内的函数生成
#         """
#          import numpy as np
#          x1 = np.arange(11)   #array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10])
#
#         """
#     3.从硬盘(文件)读取数据

"""
import numpy as np
x = np.loadtxt(r"C:\\\\Users\CZ\Desktop\Project\数据分析\000001.csv",delimiter=',',skiprows=1,useclos=(1,4,6),unpack=False)
"""

"""
使用numpy生成100以内随机数组
将数组存储到文件，再从该文件中读取数组
对数组进行排序，求最大值，最小值，均值和方差
"""
import numpy as np
x = np.random.randint(1,100,10)
np.savetxt(r"testfile.txt",x)
c= np.loadtxt(r"testfile.txt")
c_sort = np.sort(c)

highest = np.max(c)

lowest = np.min(c)
mean = np.mean(c)
variance= np.var(c)

print(c_sort,highest,lowest,mean,variance)