# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ItItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class TencentItem(scrapy.Item):
    name  = scrapy.Field()
    cate  = scrapy.Field()
    count  = scrapy.Field()
    location  = scrapy.Field()
    time  = scrapy.Field()
