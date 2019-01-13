import json
from pprint import pprint

"""
加载数据
load  文件中加载
loads 从字符串中加载


python 数据类型转换成 字符串或者文件保存

dump python数据类型保存到文件中
dumps python数据 转成 字符串

"""
#load 从json文件获取并且转成python数据类型
with open("data.json","r",encoding="utf-8") as f:
    result = json.load(f)
    pprint(result)

#loads从json字符串转成python数据类型

data = """

{ "store": {
    "book": [
      { "category": "reference",
        "author": "中文 Rees",
        "title": "Sayings of the Century",
        "price": 8.95
      },
      { "category": "fiction",
        "author": "Evelyn Waugh",
        "title": "Sword of Honour",
        "price": 12.99
      },
      { "category": "fiction",
        "author": "Herman Melville",
        "title": "Moby Dick",
        "isbn": "0-553-21311-3",
        "price": 8.99
      },
      { "category": "fiction",
        "author": "J. R. R. Tolkien",
        "title": "The Lord of the Rings",
        "isbn": "0-395-19395-8",
        "price": 22.99
      }
    ],
    "bicycle": {
      "color": "red",
      "price": 19.95
    }
  }
}
"""

result = json.loads(data)
# pprint(result)

#dumps  从python数据类型转换成字符串类型
# result = json.dumps(result)
# pprint(result)


#dump从python数据类型写入到文件中
with open("03-data.json","w",encoding="utf-8") as f:
    #写入文件
    # ensure_ascii 中文显示
    # indent 使用缩进写入
    json.dump(result,f,ensure_ascii=False,indent=2)
