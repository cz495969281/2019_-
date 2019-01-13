import requests

#POST请求
#######################################################
# data = {"name":"germey","age":22}
#
# r = requests.post("http://httpbin.org/post",data=data)
# print(r.text)

#返回结果的form部分就是提交的数据，证明POST请求成功


#响应（获取状态码,响应头,Cookies等）
r = requests.get("http://www.jianshu.com")
print(type(r.status_code),r.status_code)
print(type(r.headers),r.headers)
print(type(r.cookies),r.cookies)
print(type(r.url), r.url)
print(type(r.history), r.history)

