from bs4 import BeautifulSoup

html = """
    <html><head><title>The Dormouse's story</title></head>
    <body>
    <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
    <p class="story">Once upon a time there were three little sisters; and their names were
    <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
    <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
    and they lived at the bottom of a well.</p>
    <p class="story">...</p>
"""

#通过BeautifulSoup创建对象
#相当于xpath的根元素的对象
#自动补全标签
#bs4底层解析使用lxml默认的解析器
#自己指定解析器
soup = BeautifulSoup(html,'lxml')

#可以直接执行标签名称提取
# print(soup.title.string)


#如果有2个相同的标签，默认只获取第一个
print(soup.p)

#打印标签内容
# print(soup.prettify())