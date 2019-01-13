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
# 1. 获取所有图书信息 GET /books/
# 2. 新建一本图书信息  POST /books/

# 3. 获取指定的图书信息 GET /books/(?P<pk>\d+)/
# 4. 修改指定的图书信息 PUT /books/(?P<pk>\d+)/
# 5. 删除指定的图书信息 DELETE /books/(?P<pk>\d+)/


# /books/
# class BookInfoViewSet(mixins.ListModelMixin,
#                       mixins.CreateModelMixin,
#                       mixins.RetrieveModelMixin,
#                       mixins.UpdateModelMixin,
#                       mixins.DestroyModelMixin,
#                       GenericViewSet):
class BookInfoViewSet(ModelViewSet):
    """视图集"""
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer

