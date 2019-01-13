from lxml import etree

text = """
        <div> <ul> 
        <li class="item-1"><a href="link1.html">first item</a></li> 
        <li class="item-1"><a href="link2.html">second item</a></li> 
        <li class="item-inactive"><a href="link3.html">third item</a></li> 
        <li class="item-1"><a href="link4.html">fourth item</a></li> 
        <li class="item-0"><a href="link5.html">fifth item</a> # 注意，此处缺少一个 </li> 闭合标签 
        </ul> </div>

       """

#创建 根元素对象
#会自动创建根元素，如果没有html/body 会自动创建
#自动补全不完成的标签
root = etree.HTML(text)

#1.节点选择
# xpath方法返回的是list对象
# result = root.xpath("//li")
# print(result)

#2.文本选取
# result = root.xpath('//li[@class="item-0"]/a/text()')
# print(result)

#3.属性选取
result = root.xpath("//li/@class")
print(result)



#打印输出
# for data in result:
    # print(etree.tostring(data).decode('utf-8'))
