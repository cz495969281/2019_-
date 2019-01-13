"""

https://hr.tencent.com/position.php?&start=10#a
start 表示页数 10 递增

#爬去逻辑
1.先去获取 爬取得总职位数
2. 构建爬取 url 进行循环爬取
"""
import math

import requests
from bs4 import BeautifulSoup
import json


class TencentSpider(object):

    def __init__(self):
        self.base_url = "https://hr.tencent.com/position.php?&start={}"

        self.headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
        }

        self.items = []



    def save_items(self):
        with open("05-data.json","w",encoding="utf-8") as f:
            json.dump(self.items,f,ensure_ascii=False,indent=2)






    def run(self):

        total_page_response = requests.get(self.base_url.format(0),headers=self.headers)
        total_page_html = total_page_response.content.decode("utf-8")
        total_soup = BeautifulSoup(total_page_html,'lxml')
        total = total_soup.select('.lightblue,.total')[0].get_text()
        # print(total)

        #计算页数
        # 除以10，向上取正  ceil向上取正
        total_page = math.ceil(int(total) / 10.0)
        # print(total_page)

        for start in range(0,total_page * 10,10):
            url = self.base_url.format(start)
            list_page_response = requests.get(url,headers=self.headers)
            list_page_html = list_page_response.content.decode('utf-8')
            list_page_soup = BeautifulSoup(list_page_html,'lxml')

            rows = list_page_soup.select('.even,.odd')
            for row in rows:

                item = {}
                item["name"] = row.a.get_text()
                item["cate"] = row.find_all('td')[1].get_text()
                item["count"] = row.find_all('td')[2].get_text()
                item["location"] = row.find_all('td')[3].get_text()
                item["time"] = row.find_all('td')[4].get_text()
                self.items.append(item)
                print(item)

        self.save_items()




if __name__ == "__main__":
    spider = TencentSpider()
    spider.run()















