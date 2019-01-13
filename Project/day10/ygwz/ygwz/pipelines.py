# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
import scrapy
from pymongo import *

class YgwzPipeline(object):
    def process_item(self, item, spider):
        return item



class DouyuPipeline(ImagesPipeline):

    def open_spider(self, spider):
        super(DouyuPipeline,self).open_spider(spider)
        client = MongoClient(host="120.79.210.252",port=27017)
        self.db = client.douyu


    #重新下载图片的方法，用来让我们的item去请求图片
    def get_media_requests(self,item,info):

        #写请求图片的代码,是不保存的
        url = item["room_src"]
        yield scrapy.Request(
            url=url
        )

    #当下载完成以后会回调这个方法
    def item_completed(self, results, item, info):
        # print(results)
        item["image_path"] = [x["path"] for ok, x in results if ok][0]
        # print(item)
        self.db.items.insert(dict(item))