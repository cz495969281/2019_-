from pymongo import *


#创建客户端对象
client = MongoClient("120.79.210.252",27017)

#获取数据库对象
db = client.admin

#获取集合对象
stu = db.stu

# 增
# t2 = db.t2
# data = {
#     "aaa":"xxx",
#     "yyy":5,
#     "ddd":{
#         "q":"1",
#         "p":"2"
#     },
#     "eee":["abc","def"]
# }

# t2.insert(data)

# data = [
#     {"a":"x"},
#     {"b":"y"}
# ]
# t2.insert_many(data)


# 删
#删除某一条数据
# t2.remove({
#     "a":"x"
# })

#清空数据库
# t2.remove({})

# 改
# stu.update(
#     #查询条件
#     {
#         "age":18
#     },
#     # 更新内容
#     {
#         # "hometown":"美国"
#         "$set":{"hometown":"美国"},
#     },
#     multi=True
# )


# 查  游标的概念
cursor = stu.find(
    #查询条件
    # {
    #     "hometown":"美国"
    # }
    {
        "age":{"$gt":20}
    }
)

for doc in cursor:
    try:
        print(doc["name"])
    except Exception as e:
        pass