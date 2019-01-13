import json
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSetMixin, GenericViewSet, ModelViewSet
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import status
from django.http import Http404

from booktest.models import BookInfo
from booktest.serializers import BookInfoSerializer
# Create your views here.

# 使用Django知识自定义RestAPI接口:
# 1. 获取所有图书信息 GET /books/
# 2. 新建一本图书信息  POST /books/

# 3. 获取指定的图书信息 GET /books/(?P<pk>\d+)/
# 4. 修改指定的图书信息 PUT /books/(?P<pk>\d+)/
# 5. 删除指定的图书信息 DELETE /books/(?P<pk>\d+)/


# /books/
# class BookInfoViewSet(ViewSetMixin, GenericAPIView):
class BookInfoViewSet(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      GenericViewSet):
    """视图集"""
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer

    # GET /books/
    # def list(self, request):
    #     """获取所有图书信息"""
    #     # 查询出所有图书信息
    #     queryset = self.get_queryset()
    #
    #     # 返回所有图书信息
    #     serializer = self.get_serializer(queryset, many=True)
    #
    #     # return json
    #     return Response(serializer.data)

    # POST /books/
    # def create(self, request):
    #     """新建一本图书信息"""
    #     # 前端传递参数时，使用json传递
    #     # 获取参数(btitle, bpub_date)并进行参数校验
    #     # 反序列化-数据校验
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #
    #     # 反序列化-数据保存(create)
    #     serializer.save()
    #
    #     # 返回响应: status: 201，包含新建图书的信息
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)

    # GET /books/(?P<pk>\d+)/
    # def retrieve(self, request, pk):
    #     """获取指定的图书信息"""
    #     # 根据pk查询指定图书信息
    #     obj = self.get_object()
    #
    #     # 返回响应数据
    #     serializer = BookInfoSerializer(obj)
    #     return Response(serializer.data)

    # PUT /books/(?P<pk>\d+)/
    # def update(self, request, pk):
    #     """修改指定的图书信息"""
    #     # 根据pk查询指定图书
    #     obj = self.get_object()
    #
    #     # 前端传递参数时，使用json传递
    #     # 获取参数(btitle, bpub_date)并进行参数校验
    #     # 反序列化-数据校验
    #     serializer = self.get_serializer(obj, data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #
    #     # 反序列化-数据保存(update)
    #     serializer.save()
    #
    #     # 返回响应数据
    #     return Response(serializer.data)

    # DELETE /books/(?P<pk>\d+)/
    # def destroy(self, request, pk):
    #     """删除指定的图书信息"""
    #     # 根据pk查询指定图书
    #     obj = self.get_object()
    #
    #     # 删除图书
    #     obj.delete()
    #
    #     # 返回响应数据 status: 204
    #     return Response(status=status.HTTP_204_NO_CONTENT)

