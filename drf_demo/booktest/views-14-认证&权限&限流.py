from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.throttling import AnonRateThrottle
from booktest.models import BookInfo
from booktest.serializers import BookInfoSerializer

# 需求2：写一个视图集，提供以下两种操作
# 1. 获取一组图书信息(list) GET /books/
# 2. 获取指定图书信息(retrieve) GET /books/(?P<pk>\d+)/


# 自定义权限控制类
class MyPermission(BasePermission):
    def has_permission(self, request, view):
        """控制当前视图是否有权限进行访问，返回True代表有权限，返回False代表没权限"""
        # return False

        return True

    def has_object_permission(self, request, view, obj):
        """控制某个对象是否有权限进行访问，返回True代表有权限，返回False代表没权限"""
        # 需求: id 为 1，3的对象可以访问，其他的不允许进行访问
        if obj.id in (1, 3):
            return True

        return False


class BookInfoViewSet(ReadOnlyModelViewSet):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer

    # 指定当前视图类所采用认证方式(一旦指定，不再使用全局认证方式)
    authentication_classes = (SessionAuthentication, )

    # 指定当前视图类所采用权限控制方式(一旦指定，不再使用全局权限控制方式)
    # permission_classes = (IsAuthenticated, )

    # 使用自定义的权限控制
    # permission_classes = (MyPermission, )

    # 指定当前视图类所采用限流控制类(一旦指定，不再使用全局的)
    # throttle_classes = (AnonRateThrottle, )

    # 指定当前视图类所采用限流频次
    throttle_scope = 'contacts'
