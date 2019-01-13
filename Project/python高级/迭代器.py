# 什么是迭代协议？ 1.可迭代类型 2.迭代器
# 迭代器是什么？ 迭代器是访问集合内元素的一种方式，一般用来遍历数据

# def fun(list,n):
# 	length = len(list)
# 	for j in range(length):
# 		if list[j] == n:
# 			del list[j]
# 			list.insert(0,n)
# 	print(list)
#
# fun([10,5,8,6,7,8,9,8,19],8)

import csv
# def test(filepath):
# 	data_dict = {}
# 	com1 = []
# 	com2 = []
# 	com3 = []
# 	# csv_file = csv.reader(open(filepath,'r'))
# 	# for temp in csv_file:
# 	# 	data_dict[temp[0]] = temp[1:]
# 	# 	com1.append(temp[1])
# 	# 	com2.append(temp[2])
# 	# 	com3.append(temp[3])
# 	# sum_dict = {"sumcol2":sum(com1),"sumcol3":sum(com2),"sumcol4":sum(com3)}

	# return data_dict,sum_dict


"""
全字母短句(Pangrams)是包含所有英文字母的句子，比如："A quick brown fox jumps over the lazy dog".
定义并实现一个方法getMissingLetters；传入一个字符串参数，返回参数字符串变成
 一个Pangram中所缺失的字符。应该忽略传入字符串参数中的大小写，返回应该都是小写字符并按字母表顺序排序
 (请忽略所以非ASCII字符)
 下面示例是用来解释,双引号不需要考虑
 
 0)输入:"A quick brown fox jumps over the lazy dog"
 返回: ""
 
 1)输入:"A slow yellow fox crawls under the proactive dog"
 返回:"bjkmqz"
 
 2)输入:"Lions,and tigers,and bears,oh my!"
 返回:"cfjkpquvwxz"
 
 3)输入: ""
 返回:"abcdefghijklmnopqrstuvwxyz"
 
 
"""
def getMissingLetters(a):
    s1 = set("abcdefghijklmnopqrstuvwxyz")
    ret = ""
    s2 = set(a)
    for i in sorted(s1 - s2):
        ret += i
    return ret


print(getMissingLetters("abc"))




















