from rest_framework.generics import ListAPIView
from rest_framework.filters import OrderingFilter
from booktest.models import BookInfo
from booktest.serializers import BookInfoSerializer
# 需求：定义一个视图，只提供一个接口
# 1. 获取一组图书的信息


# 自定义分页类
from rest_framework.pagination import PageNumberPagination
from rest_framework.pagination import LimitOffsetPagination


class StandrdResultPagination(PageNumberPagination):
    # 指定默认页容量
    page_size = 3
    # 指定获取分页数据是页容量参数名字
    page_size_query_param = 'page_size'

    # 指定最大页容量
    max_page_size = 5


# /books/
class BookListView(ListAPIView):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer

    # 指定过滤字段
    filter_fields = ('btitle', 'bread')

    filter_backends = (OrderingFilter, )

    # 指定排序字段
    ordering_fields = ('id', 'bpub_date', 'bread')

    # 关闭当前视图分页
    # pagination_class = None

    # pagination_class = StandrdResultPagination
    pagination_class = LimitOffsetPagination
