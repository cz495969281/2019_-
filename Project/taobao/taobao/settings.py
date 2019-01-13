# -*- coding: utf-8 -*-

# Scrapy settings for taobao project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'taobao'

SPIDER_MODULES = ['taobao.spiders']
NEWSPIDER_MODULE = 'taobao.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'taobao (+http://www.yourdomain.com)'

# Obey robots.txt rules
# ROBOTSTXT_OBEY = False

LOG_LEVEL = 'WARNING'

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'taobao.middlewares.TaobaoSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   # 'taobao.middlewares.TaobaoDownloaderMiddleware': 543,
    'taobao.middlewares.TaobaoUserMiddleware': 544,
}
#
# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'taobao.pipelines.TaobaoPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#     'cookie': 'thw=cn; cna=VpxmFAZbMRECATomjtGMhvjN; t=3a930ddc4e45bbc7c12ddfbef5dfe533; uc3=vt3=F8dByRjC1a3KqxjCRII%3D&id2=UonZBGGzhw%2FC%2BA%3D%3D&nk2=FO4JcgXEj4Ib4%2Fx9BiE%3D&lg2=VFC%2FuZ9ayeYq2g%3D%3D; tracknick=wwcqq787663374; lgc=wwcqq787663374; _cc_=WqG3DMC9EA%3D%3D; tg=0; enc=YzQngxWyWQEB7PkMCPAkDu9y15RPXy2hngn8dGcRsTD3MHDR78DWB%2FQoN3%2Firc5WQvkodJF52A6x%2BnRrfqnIGA%3D%3D; mt=ci=61_1; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; swfstore=159907; v=0; cookie2=596d4c3f96304b935739bb9fa6fa65d3; _tb_token_=ef767b6b7386; hng=CN%7Czh-CN%7CCNY%7C156; uc1=cookie14=UoTYN4KNKBkuqg%3D%3D; JSESSIONID=D7F400C84208BC7B022250BCA27A79BE; isg=BDs7zhUJ5J2Litgps3VAazlYyh9lOE4Lpfnk1S34FzpRjFtutWDf4lnNomxnrKeK',
# }