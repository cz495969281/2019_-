# 自定义DRF框架的异常处理函数
from rest_framework.views import exception_handler as drf_exception_handler
from rest_framework.response import Response
from rest_framework import status
from django.db import DatabaseError


def exception_handler(exc, context):
    # 先调用DRF框架提供异常处理函数进行处理
    response = drf_exception_handler(exc, context)

    if response is None:
        # drf框架不能进行此异常处理
        view = context['view']
        if isinstance(exc, DatabaseError):
            # 补充数据库错误异常处理
            print('[%s]: %s' % (view, exc))
            response = Response({'detail': '服务器内部错误'}, status=status.HTTP_507_INSUFFICIENT_STORAGE)

    return response
