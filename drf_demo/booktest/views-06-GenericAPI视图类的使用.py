import json
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

from booktest.models import BookInfo, HeroInfo
from booktest.serializers import BookInfoSerializer, HeroInfoSerializer
# Create your views here.

# 使用Django知识自定义RestAPI接口:
# 1. 获取所有图书信息 GET /books/
# 2. 新建一本图书信息  POST /books/

# 3. 获取指定的图书信息 GET /books/(?P<pk>\d+)/
# 4. 修改指定的图书信息 PUT /books/(?P<pk>\d+)/
# 5. 删除指定的图书信息 DELETE /books/(?P<pk>\d+)/


# ================================ 自定义GenericAPIView视图类 ================================
class MyGenericAPIView(APIView):
    # 指定当前视图使用查询集，默认None
    queryset = None
    # 指定当前视图使用序列化器类，默认None
    serializer_class = None

    # 指定查询单个对象时，查询字段名称，默认pk
    lookup_field = 'pk'
    # 指定查询单个对象时，从url地址中提取参数的名字
    lookup_url_kwarg = 'pk'

    def get_serializer_class(self):
        """返回当前视图使用序列化器类"""
        return self.serializer_class

    def get_serializer(self, *args, **kwargs):
        """创建一个序列化器类的对象"""
        serializer_class = self.get_serializer_class()

        return serializer_class(*args, **kwargs)

    def get_queryset(self):
        """返回当前视图使用查询集"""
        return self.queryset.all()

    def get_object(self):
        """从查询集中获取指定对象"""
        queryset = self.get_queryset()

        # filters = {'pk': self.kwargs['pk']}
        filters = {self.lookup_field: self.kwargs[self.lookup_url_kwarg]}

        try:
            # obj = queryset.get(pk=<pk>)
            obj = queryset.get(**filters)
        except Exception as e:
            raise Http404

        return obj


# /books/
# class BookListView(APIView):
# class BookListView(MyGenericAPIView):
class BookListView(GenericAPIView):
    # 指定当前视图使用查询集
    # queryset = BookInfo.objects.all()
    queryset = HeroInfo.objects.all()
    # 指定当前视图使用序列化器类
    # serializer_class = BookInfoSerializer
    serializer_class = HeroInfoSerializer

    def get(self, request):
        """获取所有图书信息"""
        # 查询出所有图书信息
        # books = BookInfo.objects.all() # QuerySet(查询集)
        obj = self.get_queryset()

        # 返回所有图书信息
        # serializer = BookInfoSerializer(books, many=True)
        serializer = self.get_serializer(obj, many=True)

        # return json
        return Response(serializer.data)

    def post(self, request):
        """新建一本图书信息"""
        # 前端传递参数时，使用json传递
        # 获取参数(btitle, bpub_date)并进行参数校验
        # 反序列化-数据校验
        data = request.data
        # serializer = BookInfoSerializer(data=request.data)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # 反序列化-数据保存(create)
        serializer.save()

        # 返回响应: status: 201，包含新建图书的信息
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# /books/(?P<pk>\d+)/
# /books/10/
# class BookDetailView(APIView):
# class BookDetailView(MyGenericAPIView):
class BookDetailView(GenericAPIView):
    # 指定当前视图使用查询集
    queryset = BookInfo.objects.all()
    # 指定当前视图使用序列化器类
    serializer_class = BookInfoSerializer

    def get(self, request, pk):
        """获取指定的图书信息"""
        # 根据pk查询指定图书信息
        # try:
        #     book = BookInfo.objects.get(pk=pk)
        # except BookInfo.DoesNotExist:
        #     raise Http404
        obj = self.get_object()

        # 返回响应数据
        # serializer = BookInfoSerializer(book)
        serializer = self.get_serializer(obj)
        return Response(serializer.data)

    def put(self, request, pk):
        """修改指定的图书信息"""
        # 根据pk查询指定图书
        obj = self.get_object()

        # 前端传递参数时，使用json传递
        # 获取参数(btitle, bpub_date)并进行参数校验
        # 反序列化-数据校验
        serializer = self.get_serializer(obj, data=request.data)
        serializer.is_valid(raise_exception=True)

        # 反序列化-数据保存(update)
        serializer.save()

        # 返回响应数据
        return Response(serializer.data)

    def delete(self, request, pk):
        """删除指定的图书信息"""
        # 根据pk查询指定图书
        obj = self.get_object()

        # 删除图书
        obj.delete()

        # 返回响应数据 status: 204
        return Response(status=status.HTTP_204_NO_CONTENT)

