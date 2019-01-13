import requests

url = "https://www.baidu.com"
response = requests.get(url)
#
# #打印响应内容
# # print(response.text)
#
# print(response.content) # 响应体是bytes类型
# print(response.status_code) #响应状态码
# print(response.headers) #响应头
# print(response.request.headers) #响应对应的请求头
# # print(response.request.cookies )
# print(response.cookies)

cookies = requests.utils.dict_from_cookiejar(response.cookies)
print(cookies)

#########333333333333############################33333333


########把网络上的图片保存到本地
# import requests
#
# url ='https://www.baidu.com/img/bd_logo1.png'
# response = requests.get(url)
# print(response.content)  #bytes类型
#
# with open('baidu.png','wb') as f:
#     f.write(response.content)

######################################

####发送带header的请求

# import requests
#
# url = 'https://www.baidu.com'
# headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
# response = requests.get(url,headers=headers)
# # print(response.content)
#
# # # 打印响应对应请求的请求头信息
# print(response.request.headers)

##################################################

#  两种方式：发送带参数的请求
# import requests
#
# headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
#
# # 这是目标url
# # url = 'https://www.baidu.com/s?wd=python'
#
# # 最后有没有问号结果都一样
# url = 'https://www.baidu.com/s?'
#
# # 请求参数是一个字典 即wd=python
# kw = {'wd': 'python'}
#
#
# # 带上请求参数发起请求，获取响应
# response = requests.get(url, headers=headers, params=kw)
#
#
#
# print(response.content)














