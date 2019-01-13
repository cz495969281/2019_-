import requests

#1.文件上传
files = {'files':open('favicon.ico','rb')}
r = requests.post("http://httpbin.org/post",files=files)

#返回的响应里面包含files字段,而form字段是空的，这证明文件上传部分会单独有一个files字段来标识
print(r.text)


#2.Cookies 前面使用urllib处理过的Cookies写法复杂，而有了requests,获取和设置Cookies只需一步
requests.get("https://www.baidu.com")
print(r.cookies)
