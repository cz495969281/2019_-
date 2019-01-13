# class A(object):
# #     pass
# #
# # class B(A):
# #     pass
# #
# # b = B()
# #
# # print(type(b) != type(A))
# # print(isinstance(b, object) == True)
# # print(len(b.__dict__) == 0)
# # print(issubclass(b,B))

# def num():
#     return [lambda x: i * x for i in range(4)]
#
#
# list = [m(2) for m in num()]
#
#
# print(list)

#!/usr/bin/python3
# -*- coding: utf-8 -*-

# 1. 导入库
import requests

url = "https://www.baidu.com"

headers = {
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
}

# 2. 发送请求获取响应
response = requests.get(url,headers=headers)

# 获取内容（返回字节数据 bytes）
content = response.content

# 获取 字符串数据
# html = content.decode('utf-8')

# 更简便的方法直接获取 字符串数据
# response.encoding = 'utf-8'
html = response.text

print(type(html))


# 3. 处理响应的结果
with open('05-test.html','w+',encoding='utf-8') as f:
    f.write(html)

