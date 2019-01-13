from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import status

from booktest.models import BookInfo, HeroInfo
from booktest.serializers import BookInfoSerializer, HeroInfoSerializer
# Create your views here.

# 使用Django知识自定义RestAPI接口:
# 1. 获取所有图书信息 GET /books/
# 2. 新建一本图书信息  POST /books/

# 3. 获取指定的图书信息 GET /books/(?P<pk>\d+)/
# 4. 修改指定的图书信息 PUT /books/(?P<pk>\d+)/
# 5. 删除指定的图书信息 DELETE /books/(?P<pk>\d+)/


class MyListCreateAPIView(mixins.ListModelMixin,
                          mixins.CreateModelMixin,
                          GenericAPIView):
    def get(self, request):
        """获取所有图书信息"""
        return self.list(request)

    def post(self, request):
        """新建一本图书信息"""
        return self.create(request)


# /books/
# class BookListView(mixins.ListModelMixin,
#                    mixins.CreateModelMixin,
#                    GenericAPIView):
class BookListView(MyListCreateAPIView):
    # 指定当前视图使用查询集
    queryset = BookInfo.objects.all()
    # 指定当前视图使用序列化器类
    serializer_class = BookInfoSerializer

    # def get(self, request):
    #     """获取所有图书信息"""
    #     return self.list(request)
    #
    # def post(self, request):
    #     """新建一本图书信息"""
    #     return self.create(request)


class MyRetrieveUpdateDestroyAPIView(mixins.RetrieveModelMixin,
                                     mixins.UpdateModelMixin,
                                     mixins.DestroyModelMixin,
                                     GenericAPIView):
    def get(self, request, pk):
        """获取指定的图书信息"""
        return self.retrieve(request, pk)

    def put(self, request, pk):
        """修改指定的图书信息"""
        return self.update(request, pk)

    def delete(self, request, pk):
        """删除指定的图书信息"""
        return self.destroy(request, pk)


# /books/(?P<pk>\d+)/
# class BookDetailView(mixins.RetrieveModelMixin,
#                      mixins.UpdateModelMixin,
#                      mixins.DestroyModelMixin,
#                      GenericAPIView):
class BookDetailView(MyRetrieveUpdateDestroyAPIView):
    # 指定当前视图使用查询集
    queryset = BookInfo.objects.all()
    # 指定当前视图使用序列化器类
    serializer_class = BookInfoSerializer

    # def get(self, request, pk):
    #     """获取指定的图书信息"""
    #     return self.retrieve(request, pk)
    #
    # def put(self, request, pk):
    #     """修改指定的图书信息"""
    #     return self.update(request, pk)
    #
    # def delete(self, request, pk):
    #     """删除指定的图书信息"""
    #     return self.destroy(request, pk)

