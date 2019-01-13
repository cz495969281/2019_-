import json
import scrapy
from ygwz.items import YgwzItem
import jsonpath

from scrapy_splash.request import SplashRequest

class YgwzSpider(scrapy.Spider):
    name = "yg"
    # allow_domains = ["douyucdn.cn"]
    # start_urls = ["http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset=0"]
    allow_domains = ["tieba.baidu.com"]
    # start_urls = ["https://tieba.baidu.com/f?fr=wwwt&kw=魔兽世界&traceid="]

    # for offset in range(0,200,20):
    #     start_urls.append(base_urls.format(offset))

    def start_requests(self):
        yield SplashRequest(
            url="https://tieba.baidu.com/f?kw=魔兽世界&ie=utf-8"
        )

    def parse(self, response):
        with open("tb.html","wb") as f:
            f.write(response.body)
        print(response.xpath('//div[@class="threadlist_abs threadlist_abs_onlyline "]/text()').extract_first())
        pass

    # def parse(self, response):
    #
    #     data = json.loads(response.body.decode("utf-8"))
    #     print(data)
    #     room_id_list = jsonpath.jsonpath(data,"$..room_id")
    #     room_src_list =jsonpath.jsonpath(data,"$..room_src")
    #     room_name_list =jsonpath.jsonpath(data,"$..room_name")
    #
    #     for room_id,room_src,room_name in zip(room_id_list,room_src_list,room_name_list):
    #         item = YgwzItem()
    #         item["room_id"] = room_id
    #         item["room_src"] = room_src
    #         item["room_name"] = room_name
    #         # print(room_id,room_src,room_name)
    #         yield item
    #
    #
    #     pass
