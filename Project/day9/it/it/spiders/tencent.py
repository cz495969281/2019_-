# -*- coding: utf-8 -*-
import scrapy
from it.items import TencentItem

class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['jianshu.com']
    start_urls = ['https://www.jianshu.com/']


    def start_requests(self):
        cookies_string = 'read_mode=day; default_font=font2; locale=zh-CN; Hm_lvt_0c0e9d9b1e7d617b3e6842e85b9fb068=1537085841,1537151151,1537955676,1538030836; _m7e_session=ef872008e3b25d2778af2888b6e6fa7c; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221657b7a0c4d29b-0555ee44406fb8-37664109-1327104-1657b7a0c4e88%22%2C%22%24device_id%22%3A%221657b7a0c4d29b-0555ee44406fb8-37664109-1327104-1657b7a0c4e88%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Flink%22%2C%22%24latest_referrer_host%22%3A%22www.baidu.com%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%7D%2C%22first_id%22%3A%22%22%7D; signin_redirect=https%3A%2F%2Fwww.jianshu.com%2F; Hm_lpvt_0c0e9d9b1e7d617b3e6842e85b9fb068=1538032385'
        cookies = dict([[cookie_str.split('=')[0],cookie_str.split('=')[1]] for cookie_str in cookies_string.split('; ')])

        yield scrapy.Request(
            url="https://www.jianshu.com/",
            cookies=cookies
        )

    def parse(self, response):
        with open('login1.html', 'w', encoding='utf-8') as f:
            f.write(response.text)


"""
read_mode=day; default_font=font2; locale=zh-CN; Hm_lvt_0c0e9d9b1e7d617b3e6842e85b9fb068=1537085841,1537151151,1537955676,1538030836; _m7e_session=ef872008e3b25d2778af2888b6e6fa7c; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221657b7a0c4d29b-0555ee44406fb8-37664109-1327104-1657b7a0c4e88%22%2C%22%24device_id%22%3A%221657b7a0c4d29b-0555ee44406fb8-37664109-1327104-1657b7a0c4e88%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Flink%22%2C%22%24latest_referrer_host%22%3A%22www.baidu.com%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%7D%2C%22first_id%22%3A%22%22%7D; signin_redirect=https%3A%2F%2Fwww.jianshu.com%2F; Hm_lpvt_0c0e9d9b1e7d617b3e6842e85b9fb068=1538032385
"""