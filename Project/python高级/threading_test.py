import threading
import time
from concurrent.futures import ThreadPoolExecutor,as_completed
import requests

# submit
"""
def add(n1,n2):
    v = n1 + n2
    print("add:",v,"tid:",threading.currentThread().ident)
    time.sleep(n1)
    return v

#通过submit 把需要执行的函数扔进线程池中
#submit 直接返回一个future对象

ex = ThreadPoolExecutor(max_workers=3)  #制定最多运行N个线程
f1 = ex.submit(add,2,3)
f2 = ex.submit(add,2,3)
print('main thread running')
print(f1.done())   #done 看看任务结束了没
# print(f1.result())    #获取结果 ,阻塞方法

"""

#map
"""
URLS = ['http://www.baidu.com', 'http://www.qq.com', 'http://www.sina.com.cn']

def get_html(url):
    print('thread id:', threading.currentThread().ident, ' 访问了:', url)
    return requests.get(url)

ex = ThreadPoolExecutor(max_workers=3)
res_iter = ex.map(get_html,URLS)
print(res_iter)
for res in res_iter:
    print("url:%s ,len:%d"%(res.url,len(res.text)))
    print(res)
"""

#as_completed
"""
URLS = ['http://www.baidu.com', 'http://www.qq.com', 'http://www.sina.com.cn']

def get_html(url):
    time.sleep(3)
    print('thread id:', threading.currentThread().ident, ' 访问了:', url)
    return requests.get(url)

ex = ThreadPoolExecutor(max_workers=3)
f = ex.submit(get_html,URLS[0])
print("main thread runing")

for future in as_completed([f]):  #as_completed()接受一个可迭代的Future序列,返回一个生成器,在完成或异常时返回这个Future对象
    print("一个任务完成")
    print(future.result())


"""

from multiprocessing import Manager

#Semaphore 是用于控制进入数量的锁
#文件， 读、写， 写一般只是用于一个线程写，读可以允许有多个

#做爬虫
# import threading
# import time
#
# class HtmlSpider(threading.Thread):
#     def __init__(self, url, sem):
#         super().__init__()
#         self.url = url
#         self.sem = sem
#
#     def run(self):
#         time.sleep(2)
#         print("got html text success")
#         self.sem.release()
#
# class UrlProducer(threading.Thread):
#     def __init__(self, sem):
#         super().__init__()
#         self.sem = sem
#
#     def run(self):
#         for i in range(20):
#             self.sem.acquire()
#             html_thread = HtmlSpider("https://baidu.com/{}".format(i), self.sem)
#             html_thread.start()
#
# if __name__ == "__main__":
#     sem = threading.Semaphore(3)
#     url_producer = UrlProducer(sem)
#     url_producer.start()
def test(a, b):

    sa = set(a)
    sb = set(b)


    if sa == sb:
        for x in sa:
            if a.count(x) != b.count(x):
                return False
        return True

    else:
        return False


if __name__ == '__main__':

    a = "gabcdabcd"
    b = "aagbbccdd"
    res = test(a, b)
    print(res)