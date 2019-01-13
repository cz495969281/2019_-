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

# 通过BeautifulSoup创建对象
# 相当于xpath的根元素的对象
# 自动补全标签
# bs4底层解析使用lxml默认的解析器
# 自己指定解析器
soup = BeautifulSoup(html, 'lxml')

#1.获取节点
title_node = soup.title

#2.获取文本内容get_text()，获取的文本内容
# print(title_node.get_text())

#3.获取属性get("属性名称")
# 如果属性是class 就会返回列表
print(soup.p.get("name"))
print(soup.p.get("class"))











