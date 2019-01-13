from bs4 import BeautifulSoup

html = """
    <html><head><title>The Dormouse's story</title></head>
    <body>
    <p class="title cls" name="dromouse"><b>The Dormouse's story</b></p>
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

#find方法，只查询第一个
#通过标签查询
# result = soup.find('p')
# print(result)

#通过属性
# result = soup.find(attrs={
#     "name":"dromouse"
# })
# print(result)

#通过内容查询
# result = soup.find(text="The Dormouse's story")
# print(result)


#标签 + 属性 + 内容可以一起查询
# result = soup.find(
#     'a',
#     attrs={
#         "class":"sister"
#     },
#     text= "Tillie"
# )
# print(result.get_text())


#find_all 方法  查询所有的,属性查询，内容查询，混合一起查询和find一致
#find_all 返回是列表    支持多标签查询
# result = soup.find_all(["p","a"])
# print(result)

# result = soup.find_all(
#     ['b','a'],
#     attrs={
#         'class':'sister'
#     },
#     text="Tillie"
# )
# print(result)


# 1.标签选择器
# result = soup.select('a')
# 2.类选择器
#    单个类选择器
result = soup.select('.title')
#    多个类选择器  中间不带空格 并级，如果带空格 表示子孙级别选择
result = soup.select('.title .cls')
#    多个平行类选择器
result = soup.select('.title,.story')
# 3.ID选择器
result = soup.select("#link1")
# 4.层级选择器
    #p标签下的所有子孙 a 中间是空格就是子孙关系
result = soup.select('p a')

    # 儿子关系
result = soup.select('p > b')

    #或关系
result = soup.select('p,b')


# 5.属性选择器
result = soup.select('p[name="dromouse"]')
print(result)