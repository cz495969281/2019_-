
"""
分析
url  https://m.douban.com/rexxar/api/v2/subject_collection/filter_tv_american_hot/items
请求方式 get
请求参数
    start 开始位置
    count 请求数量
请求头 User-Agent
     Referer

"""
import json
from pprint import pprint

import jsonpath
import requests


class AmericanTVSpider(object):
    def __init__(self):
        self.base_url = "https://m.douban.com/rexxar/api/v2/subject_collection/filter_tv_american_hot/items"
        self.count = 18
        self.headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
            "Referer":"https://m.douban.com/tv/american"
        }

    def run(self):
        #循环获取url列表
        for start in range(0,1000*self.count,self.count):
            params = {
                'start':start,
                "count":self.count
            }
            response= requests.get(self.base_url,headers=self.headers,params=params)
            # print(response.content.decode('utf-8'))
            result = response.content.decode("utf-8")
            result = json.loads(result)
            # pprint(result)
            titles = jsonpath.jsonpath(result,"$..title")
            pprint(titles)
if __name__ == "__main__":
    spider = AmericanTVSpider()
    spider.run()