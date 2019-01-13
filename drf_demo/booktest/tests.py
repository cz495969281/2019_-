import os
import json

# 设置Django运行所依赖的环境变量
if not os.environ.get('DJANGO_SETTINGS_MODULE'):
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "drf_demo.settings")

# 让django进行一次初始化
import django
django.setup()


from booktest.serializers import BookInfoSerializer, HeroInfoSerializer
from booktest.models import BookInfo, HeroInfo


if __name__ == "__main__":
    # 使用DRF router自动生成视图集处理函数的url配置项
    from rest_framework.routers import SimpleRouter, DefaultRouter
    # router = SimpleRouter()
    router = DefaultRouter()

    # 注册视图集
    from booktest.views import BookInfoViewSet
    router.register('books', BookInfoViewSet, base_name='books')

    # 获取自动生成的url配置项列表
    for url in router.urls:
        print(url)

# if __name__ == "__main__":
#     # serializer = BookInfoSerializer()
#     # print(serializer)
#
#     serializer = HeroInfoSerializer()
#     print(serializer)

# if __name__ == "__main__":
#     book = BookInfo.objects.get(id=1)
#
#     # 要求图书阅读量必须大于等于评论量
#     # data = {'btitle': '射雕英雄传222', 'bpub_date': '2010-1-1'}
#     data = {'btitle': '射雕英雄传22222'}
#
#     # 创建序列化器的对象
#     serializer = BookInfoSerializer(book, data=data, partial=True)
#     print(serializer.is_valid())
#     print(serializer.errors)
#     print(serializer.validated_data)
#
#     # 数据保存
#     book = serializer.save(name='laowang') # update
#     print(book)


# if __name__ == "__main__":
#     # 要求图书阅读量必须大于等于评论量
#     data = {'btitle': 'Django入门', 'bpub_date': '2010-1-1'}
#
#     # 创建序列化器的对象
#     serializer = BookInfoSerializer(data=data)
#     print(serializer.is_valid())
#     print(serializer.errors)
#     print(serializer.validated_data)
#
#     # 数据保存
#     book = serializer.save() # create
#     print(book)


# if __name__ == "__main__":
#     # data = {'bpub_date': 123}
#
#     # data = {'btitle': 'python', 'bpub_date': '2010-1-1'}
#     # data = {'btitle': 'Django入门', 'bpub_date': '2010-1-1'}
#     # 要求图书阅读量必须大于等于评论量
#     data = {'btitle': 'Django入门', 'bpub_date': '2010-1-1', 'bread': 21, 'bcomment': 20}
#
#     # 创建序列化器的对象
#     serializer = BookInfoSerializer(data=data)
#     print(serializer.is_valid())
#     print(serializer.errors)
#     print(serializer.validated_data)


# if __name__ == "__main__":
#     # ======================== 关联对象嵌套序列化(多个关联对象) ========================
#     # 获取id为1的图书
#     book = BookInfo.objects.get(id=1)
#     # print(book)
#     # print(book.heroinfo_set.all())
#
#     # 创建序列化器对象
#     serializer = BookInfoSerializer(book)
#
#     res = json.dumps(serializer.data, ensure_ascii=False, indent=1)
#     print(res)

# if __name__ == "__main__":
#     # ======================== 关联对象嵌套序列化(单个关联对象) ========================
#     # 获取id为1的英雄
#     hero = HeroInfo.objects.get(id=1)
#
#     # hero.hbook 获取和hero对象关联的图书
#     # print(hero.hbook)
#     # print(hero.hbook.id)
#
#     # 创建序列化器对象
#     serializer = HeroInfoSerializer(hero)
#     # print(serializer.data)
#
#     res = json.dumps(serializer.data, ensure_ascii=False, indent=1)
#     print(res)


# if __name__ == "__main__":
#     # ======================== 序列化多个对象 ========================
#     # 获取所有图书
#     qs = BookInfo.objects.all()
#
#     # 创建序列化器对象
#     serializer = BookInfoSerializer(qs, many=True)
#
#     print(serializer.data)
#
#     res = json.dumps(serializer.data, ensure_ascii=False, indent=1)
#     print(res)

# if __name__ == "__main__":
#     # ======================== 序列化单个对象 ========================
#     # 查询id为1的图书
#     book = BookInfo.objects.get(id=1)
#
#     # 创建序列化器类的对象
#     serializer = BookInfoSerializer(book)
#
#     print(serializer.data)
#
#     res = json.dumps(serializer.data, ensure_ascii=False, indent=1)
#     print(res)
