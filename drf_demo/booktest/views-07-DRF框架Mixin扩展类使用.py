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


# =========================== 自定义Mixin扩展类 ===========================
class MyListModelMixin(object):
    def list(self, request, *args, **kwargs):
        """提供一组信息的通用流程"""
        # 查询出所有图书信息
        queryset = self.get_queryset()

        # 返回所有图书信息
        serializer = self.get_serializer(queryset, many=True)

        # return json
        return Response(serializer.data)


class MyCreateModelMixin(object):
    def create(self, request, *args, **kwargs):
        """创建一条数据的通用流程"""
        # 前端传递参数时，使用json传递
        # 获取参数(btitle, bpub_date)并进行参数校验
        # 反序列化-数据校验
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # 反序列化-数据保存(create)
        serializer.save()

        # 返回响应: status: 201，包含新建图书的信息
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# /books/
# class BookListView(MyListModelMixin,
#                    MyCreateModelMixin,
#                    GenericAPIView):
class BookListView(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   GenericAPIView):
    # 指定当前视图使用查询集
    queryset = BookInfo.objects.all()
    # queryset = HeroInfo.objects.all()
    # 指定当前视图使用序列化器类
    serializer_class = BookInfoSerializer
    # serializer_class = HeroInfoSerializer

    def get(self, request):
        """获取所有图书信息"""
        return self.list(request)

    def post(self, request):
        """新建一本图书信息"""
        return self.create(request)


# =========================== 自定义Mixin扩展类 ===========================
class MyRetrieveModelMixin(object):
    def retrieve(self, request, *args, **kwargs):
        """获取一条数据的通用流程"""
        # 根据pk查询指定图书信息
        obj = self.get_object()

        # 返回响应数据
        serializer = self.get_serializer(obj)
        return Response(serializer.data)


class MyUpdateModelMixin(object):
    def update(self, request, *args, **kwargs):
        """更新一条数据的通用流程"""
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


class MyDestroyModelMixin(object):
    def destroy(self, request, *args, **kwargs):
        """删除一条数据的通用流程"""
        # 根据pk查询指定图书
        obj = self.get_object()

        # 删除图书
        obj.delete()

        # 返回响应数据 status: 204
        return Response(status=status.HTTP_204_NO_CONTENT)


# /books/(?P<pk>\d+)/
# class BookDetailView(MyRetrieveModelMixin,
#                      MyUpdateModelMixin,
#                      MyDestroyModelMixin,
#                      GenericAPIView):
class BookDetailView(mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     GenericAPIView):
    # 指定当前视图使用查询集
    queryset = BookInfo.objects.all()
    # 指定当前视图使用序列化器类
    serializer_class = BookInfoSerializer

    def get(self, request, pk):
        """获取指定的图书信息"""
        return self.retrieve(request, pk)

    def put(self, request, pk):
        """修改指定的图书信息"""
        return self.update(request, pk)

    def delete(self, request, pk):
        """删除指定的图书信息"""
        return self.destroy(request, pk)

