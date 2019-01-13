from rest_framework.viewsets import ModelViewSet

from booktest.models import BookInfo
from booktest.serializers import BookInfoSerializer
# 使用DRF框架定义RestAPI接口:
# 1. 获取所有图书信息 GET /books/
# 2. 新建一本图书信息  POST /books/
# 3. 获取指定的图书信息 GET /books/(?P<pk>\d+)/
# 4. 修改指定的图书信息 PUT /books/(?P<pk>\d+)/
# 5. 删除指定的图书信息 DELETE /books/(?P<pk>\d+)/


class BookInfoViewSet(ModelViewSet):
    """视图集"""
    queryset = BookInfo.objects.all()
    # 序列化器类
    serializer_class = BookInfoSerializer
