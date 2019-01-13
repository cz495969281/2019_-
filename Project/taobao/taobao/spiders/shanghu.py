# -*- coding: utf-8 -*-
import re

import scrapy


class ShanghuSpider(scrapy.Spider):
    name = 'shanghu'
    allowed_domains = ['taobao.com']
    start_urls = ['https://shopsearch.taobao.com/search?app=shopsearch&search_type=shop']

    def parse(self, response):
        html = response.text
        # 获取店铺分类
        classifys = re.findall(r'{"name":".*?","domClass":".*?","url":"(.*?)"', html)
        for classify_url in classifys:
            classify_url = 'https://shopsearch.taobao.com' + classify_url.encode('utf-8').decode("unicode_escape")
            yield scrapy.Request(
                url=classify_url,
                callback=self.shop_list_parse,
            )
            # break

    def shop_list_parse(self, response):
        html = response.text
        #shop_pages_num 正则出淘宝店铺列表的数量
        shop_pages_num = re.findall(r'{"totalHits":(\d*?),"isSimilar":false}', html)
        try:
            #获取该店铺分类下的总数
            num = int(shop_pages_num[0])
        except:
            pass
        # print(num)
        """
        url 拼接获取所有店铺列表页
        """
        for page in range(20,num,20):
            classify_url = response.url + '&s={}'
            yield scrapy.Request(
                url= classify_url.format(page),
                callback=self.shop_detail_parse
            )
            break

    def shop_detail_parse(self,response):
        html = response.text
        # 获取店铺详情页url
        shop_urls = re.findall(r'"shopUrl":"(.*?)","similarUrl"', html)
        for shop_url in shop_urls:
            print(shop_url)
