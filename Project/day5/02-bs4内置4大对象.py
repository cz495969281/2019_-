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

#1. BeautifulSoup对象 表示根对象
print(type(soup))

#2. Tag对象 标签对象
title = soup.title
print(type(title))

#3. NavigableString  内容对象
content = soup.title.string
print(type(content))

#4.Comment表示html内容注释对象
a_content= soup.a.string
print(type(a_content))

# 2个属性
#获取标签迭代器可以循环遍历
# children = soup.body.children
# for child in children:
#     print(child)

#返回子元素的内容 列表数据，contents也是获取子元素
contents= soup.body.contents
for content in contents:
    print("*"*50)
    print(content)


"""
都是获取标签子元素列表
children         和       contents 区别
返回的事迭代器               返回的事列表
过滤换行符                   不过滤换行符

"""