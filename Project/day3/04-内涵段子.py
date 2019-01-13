#https://www.neihan8.com/e/action/ListInfo/?classid=11&page=1093

# 爬取思路：
#  先获取列表页 --> 提取详情链接 -->提取详情页的内容
from pprint import pprint
import requests
import re
from html.parser import HTMLParser

class Neihan8Spider(object):
    def __init__(self):
        self.base_url = "https://www.neihan8.com/e/action/ListInfo/?classid=11&page={}"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
        }
        self.site_url = "https://www.neihan8.com/"

    def save(self,content):
        #保存
        print(content)
        print("*"*100)
    def run(self):

        html_parser = HTMLParser()
        #提取详情页url地址的正则表达式
        detail_page_url_pattern = re.compile(r'<a href="(.*?)" class="title" title')


        #详情页初步提取的正则表达式
        detail_content_pattern = re.compile(r'<div class="detail">(.*?)<div class="tag-share line">',re.RegexFlag.DOTALL)

        #精准提取内容的正则
        detail_part_pattern = re.compile(r"<p>(.*?)</p>")


        # 1.循环获取列表数据
        list_page_urls = [self.base_url.format(page) for page in range(1094)]
        # pprint(list_urls)

        for list_page_url in list_page_urls:
            #2.获取列表页面的html数据
            response = requests.get(list_page_url,headers = self.headers)

            # list_page_html = response.content.decode('utf-8')
            list_page_html = response.text

            detail_page_urls = detail_page_url_pattern.findall(list_page_html)
            # pprint(detail_page_urls)

            #3继续访问详情页面
            for detail_page_url in detail_page_urls:
                url = self.site_url + detail_page_url
                detail_response = requests.get(url, headers=self.headers)
                detail_html = detail_response.content.decode('utf-8')
                #4提取内容
                #4.1提取初步的内容
                detail_contents = detail_content_pattern.findall(detail_html)
                if len(detail_contents) > 0:
                    detail_content = detail_contents[0]
                    parts = detail_part_pattern.findall(detail_content)
                    content = ""
                    for part in parts:
                        #处理html的转义字符
                        #scape
                        part = html_parser.unescape(part)
                        part = part.strip()
                        content += part + "\n"
                    self.save(content)



            # break
if __name__ == "__main__":
    spider = Neihan8Spider()
    spider.run()