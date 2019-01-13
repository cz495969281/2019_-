
import requests
from  retrying import retry

# stop_max_attempt_number 重试的次数
@retry(stop_max_attempt_number=3)
def parse_url(url):
# url = "http://www.12306.cn/mormhweb/"

    headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
    }

    proxies = {
        "http":"186.42.215.30:53284"
    }
    response = requests.get(url,headers=headers,proxies=proxies,verify=False)

    with open("01-reqest_https.html","wb") as f:
        f.write(response.content)

if __name__ == "__main__":
    parse_url("http://www.baidu.com")