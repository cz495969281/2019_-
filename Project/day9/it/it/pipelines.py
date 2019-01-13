# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

"""
这里文件填写保存数据的代码
要实现自定义保存数据

1.创建对象并且 实现 process_item的方法

2.在配置文件中设置 管道对象
在settings.py中配置  ITEM_PIPELINES 列表中添加 管道类

在process_item 中必须把item返回，因为数据流必须往下执行

在ITEM_PIPELINES 中的配置的值数字是表示优先级，数字越小优先级越高
"""
class ItPipeline(object):
    # process_item() 引擎自动调用，这个函数是固定的，所以不能改变
    def process_item(self, item, spider):
        # print(spider.name)

        return item

# 自定义JSON数据
class ItcastJsonPipeline(object):

    #当爬虫启动时执行回调
    def open_spider(self,spider):
        self.f = open("mydata.json","w",encoding='utf-8')
        self.f.write("[")


    #当引擎接收item对象执行一次
    def process_item(self, item, spider):
        json.dump(item,self.f,ensure_ascii=False,indent=2)
        self.f.write(",")

    #当爬虫结束时回调一次
    def close_spider(self,spider):
        self.f.write("]")
        self.f.close()












