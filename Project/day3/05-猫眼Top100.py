import re

import requests

def get_one_page(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
    }
    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        return response.text
    return None


def parse_one_page(html):
    # print(html)
    patterns = re.compile(
        # '<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?start.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>',
        '<dd>.*?board-index.*?>(.*?)</i>',
        re.S
    )
    # print(patterns)
    items = re.findall(patterns,html)
    print(items)


def main():
    url = "http://maoyan.com/board/4"
    html = get_one_page(url)
    # print(html)
    parse_one_page(html)
main()

"""
<dd>.*?board-index.*?>(.*?)</i>  提取排名信息
<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)"  提取图片
<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?</a>  提取电影的名字
# <dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?</a>.*?start.?*>(.?*)</p>.*?releasetime(.?*)</p>.*?integer.?*>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>  提取主演，发布时间，评分等内容
"""

