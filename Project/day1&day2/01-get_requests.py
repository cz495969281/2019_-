
#############################################
import requests

# r = requests.get("https://www.baidu.com/")
# print(type(r))
# print(r.status_code)
#
# print(type(r.text))
# print(r.text)
# print(r.cookies)

#############################################



# import requests

data = {
    "name":"germey",
    "age":22
}
r = requests.get("http://httpbin.org/get",params=data)

#网页的返回类型实际上是str的类型，但是它很特殊，是JSON格式，所以，如果想直接返回结果，得到一个字典格式的话,可以直接调用Json()方法
# 调用json()方法，就可以将返回结果是JSON格式的字符串转化为字典
#
# print(r.text)
# print(type(r.text))
# print(r.json())
# print(type(r.json()))

###################################################

#抓取网页 &&& 添加headers

# import requests
# import re
#
# headers = {
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
# }
#
# r = requests.get("https://www.zhihu.com/explore",headers=headers)
# pattern = re.compile("explore-feed.*?question_link.*?>(.*?)</a>",re.S)
# titles = re.findall(pattern,r.text)
#
# print(titles)


###########################################################

#抓取二进制数据

import requests

r = requests.get("https://github.com/favicon.ico")
with open("favicon.ico","wb") as f:
    f.write(r.content)

## r.text返回的是str数据类型
## r.content返回是bytes数据类型