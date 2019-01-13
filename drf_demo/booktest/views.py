import json
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSetMixin, GenericViewSet, ModelViewSet, ReadOnlyModelViewSet
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import status
from django.http import Http404

from booktest.models import BookInfo
from booktest.serializers import BookInfoSerializer
# Create your views here.

# 使用Django知识自定义RestAPI接口:
# 1. 获取所有图书信息(list) GET /books/
# 2. 新建一本图书信息(create)  POST /books/
# 3. 获取指定的图书信息(retrieve) GET /books/(?P<pk>\d+)/
# 4. 修改指定的图书信息(update) PUT /books/(?P<pk>\d+)/
# 5. 删除指定的图书信息(destroy) DELETE /books/(?P<pk>\d+)/


# /books/
class BookInfoViewSet(ModelViewSet):
    """
    list: 获取图书列表信息
    create: 创建一本图书信息
    retrieve: 获取指定的图书信息
    update: 修改指定的图书信息
    delete: 删除指定的图书信息
    """
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer

    # 在当前视图集中增加两个额外操作:
    # 1. 获取最新发布的图书信息 GET /books/latest/
    # 2. 修改指定图书的阅读量(只修改阅读量) PUT /books/(?P<pk>\d+)/read/
    # GET /books/latest/
    def latest(self, request):
        """获取最新发布的图书信息"""
        book = BookInfo.objects.latest('id')

        # 将图书数据序列化并返回
        serializer = self.get_serializer(book)
        return Response(serializer.data)

    # PUT /books/(?P<pk>\d+)/read/
    def read(self, request, pk):
        """修改指定图书的阅读量(只修改阅读量)"""
        # 获取指定的图书
        book = self.get_object()

        # 获取修改阅读量参数
        bread = request.data.get('bread')

        # 更新
        book.bread = bread
        book.save()

        # 返回
        serializer = self.get_serializer(book)
        return Response(serializer.data)

