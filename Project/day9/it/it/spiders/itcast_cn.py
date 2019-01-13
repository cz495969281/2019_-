# -*- coding: utf-8 -*-
import scrapy


#1.集成scrapy.Spider 是爬虫组件
class ItcastCnSpider(scrapy.Spider):
    #2.爬虫名称
    name = 'itcast.cn'

    #3允许域名 如果爬虫的url不再这个域名中就不爬取
    allowed_domains = ['http://www.itcast.cn/']

    #4.请求一开始的url地址列表
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    # 5.当请求完成获取response后，引擎传递给我们的响应对象并且引擎自动回调
    def parse(self, response):

        # response.xpath 返回的是一个selector对象
        # selector 封装所以数据提取的方法(xpath,css)

        #所有提取的结果都是selector对象
        #如果想获取真实数据就要从selector对象中提取具体数据
        #selector.extract()

        #xpath 和css 方法返回的都是 列表对象
        # teacher_list = response.xpath('//div[@class="tea_con"]')
        # for li in teacher_list:
        #     names = li.xpath('.//div[@class="li_txt"]/h3/text()')
        #     for name in names:
        #         print(name.extract())

        divs = response.xpath('//div[@class="li_txt"]')
        for div in divs:
            #xpath 返回的列表，如果列表执行extract() 返回的事列表内容
            #extract_first 提取第一个元素的内容
            #extract_first 防止数据为空的情况下访问下表越界
            item = {}
            item["name"] = div.xpath("./h3/text()").extract_first()
            item["type"] = div.xpath("./h4/text()").extract_first()
            item["desc"] = div.xpath("./p/text()").extract_first()
            # print(item)

            #保存数据 --> 提交给引擎 -->只需要使用一个大家都喜欢的关键词yeild
            #scrapy 提供了系统保存方案
            # 运行爬虫时指定输入文件，会根据后缀名自动生成  scrapy crawl -o "文件名"
            yield item

























