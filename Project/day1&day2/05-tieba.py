#kw ：贴吧名称
#pn ：页数
# https://tieba.baidu.com/f?ie=utf-8&kw=%E4%B8%9C%E5%93%A5&fr=search
import requests
url = "https://tieba.baidu.com/f"

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
}

kw = input("请输入贴吧名称:")

for pn in range(0,150,50):
    params = {
        "kw":kw,
        "pn":pn,
        "ie":"utf-8"
    }
    response = requests.get(url,params=params,headers=headers)
    with open("01-sample-{}.html".format(pn),'w',encoding='utf-8')as f:
        f.write(response.text)


