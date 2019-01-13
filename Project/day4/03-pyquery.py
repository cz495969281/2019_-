

# html = '''
# <div>
#     <ul>
#          <li class="item-0">first item</li>
#          <li class="item-1"><a href="link2.html">second item</a></li>
#          <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
#          <li class="item-1 active"><a href="link4.html">fourth item</a></li>
#          <li class="item-0"><a href="link5.html">fifth item</a></li>
#      </ul>
#  </div>
# '''
# from pyquery import PyQuery as pq

# 字符串初始化
# doc = pq(html)
# print(doc('li'))

# URL初始化
# doc = pq(url="http://cuiqingcai.com")
# print(doc('title'))

# 文件初始化
# doc = pq(filename='05-test.html')
# print(doc('li'))


# 3. 基本CSS选择器
# html = '''
# <div id="container">
#     <ul class="list">
#          <li class="item-0">first item</li>
#          <li class="item-1"><a href="link2.html">second item</a></li>
#          <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
#          <li class="item-1 active"><a href="link4.html">fourth item</a></li>
#          <li class="item-0"><a href="link5.html">fifth item</a></li>
#      </ul>
#  </div>
# '''
#
# from pyquery import PyQuery as pq
#
# doc = pq(html)
# print(doc('#container .list li'))
# print(type(doc('#container .list li'))) PyQuery类型。


# 4. 查找节点

# 4.1 子节点
# from pyquery import PyQuery as pq
# doc = pq(html)
# item = doc('.list')
# print(item)
# lis = item.find('li')  #find()方法会将符合条件的所有节点选择出来，结果的类型是PyQuery类型
# print(lis)
# print(type(lis))

# 其实find()的查找范围是节点的所有子孙节点，而如果我们只想查找子节点，那么可以用children()方法
# lis = item.children('.active')
# print(type(lis))
# print(lis)

# 父节点

html = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
             <li class="item-0">first item</li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div>
 </div>
'''

from pyquery import PyQuery as pq
# doc = pq(html)
# items = doc('.list')
# container = items.parent()

# 这里的父节点是该节点的直接父节点，也就是说，它不会再去查找父节点的父节点，即祖先节点。
# print(type(container))
# print(container)

# parents()方法会返回所有的祖先节点。
# parents = items.parents()
# print(type(parents))
# print(parents)

# parent = items.parents('.wrap')
# print(parent)

# 兄弟节点
# 取兄弟节点 使用siblings()方法
# doc = pq(html)
# li = doc('.list .item-0.active')
# print(li.siblings())

# 可以向siblings方法传入CSS选择器，这样就会从所有兄弟节点中挑选出符合条件的节点
# print(li.siblings('.active'))


#遍历

# doc = pq(html)
# # 调用items()方法后，会得到一个生成器
# lis = doc('li').items()
# print(type(lis))
# for li in lis:
#     print(li,type(li))


#获取属性
from pyquery import PyQuery as pq
doc = pq(html)
# a = doc('.item-0.active a')
# print(a,type(a))
# print(a.attr('href'))

a = doc("a")
# 调用attr()方法时，返回结果却只是第一个。这是因为，当返回结果包含多个节点时，调用attr()方法，只会得到第一个节点的属性
# print(a)
# print(a.attr("href"))


#在进行属性获取时，可以观察返回节点是一个还是多个，如果是多个，则需要遍历才能依次获取每个节点的属性
# a = doc('a')
# for item in a.items():
#     print(item.attr('href'))