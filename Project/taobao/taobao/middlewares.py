# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import json

from scrapy import signals

class TaobaoUserMiddleware(object):
    def process_request(self, request, spider):
        b = 'thw=cn; cna=VpxmFAZbMRECATomjtGMhvjN; t=3a930ddc4e45bbc7c12ddfbef5dfe533; uc3=vt3=F8dByRjC1a3KqxjCRII%3D&id2=UonZBGGzhw%2FC%2BA%3D%3D&nk2=FO4JcgXEj4Ib4%2Fx9BiE%3D&lg2=VFC%2FuZ9ayeYq2g%3D%3D; tracknick=wwcqq787663374; lgc=wwcqq787663374; _cc_=WqG3DMC9EA%3D%3D; tg=0; enc=YzQngxWyWQEB7PkMCPAkDu9y15RPXy2hngn8dGcRsTD3MHDR78DWB%2FQoN3%2Firc5WQvkodJF52A6x%2BnRrfqnIGA%3D%3D; mt=ci=61_1; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; swfstore=159907; v=0; cookie2=596d4c3f96304b935739bb9fa6fa65d3; _tb_token_=ef767b6b7386; hng=CN%7Czh-CN%7CCNY%7C156; uc1=cookie14=UoTYN4KNKBkuqg%3D%3D; JSESSIONID=D7F400C84208BC7B022250BCA27A79BE; isg=BDs7zhUJ5J2Litgps3VAazlYyh9lOE4Lpfnk1S34FzpRjFtutWDf4lnNomxnrKeK'

        cookie = {}
        for line in b.split(';'):
            key, value = line.split('=', 1)
            cookie[key] = value
        request.cookies = cookie
        return None


class TaobaoSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class TaobaoDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
