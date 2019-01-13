from django.conf.urls import url
from booktest import views


urlpatterns = [
    # url(r'^books/$', views.BookInfoViewSet.as_view({
    #     'get': 'list',
    #     'post': 'create'
    # }), name='books-list'),
    # url(r'^books/(?P<pk>\d+)/$', views.BookInfoViewSet.as_view({
    #     'get': 'retrieve',
    #     'put': 'update',
    #     'delete': 'destroy'
    # }), name='books-detail'),
    # url(r'^books/latest/$', views.BookInfoViewSet.as_view({
    #     'get': 'latest'
    # }), name='books-latest'),
    # url(r'^books/(?P<pk>\d+)/read/$', views.BookInfoViewSet.as_view({
    #     'put': 'read'
    # }), name='books-read')
]

# 使用DRF router自动生成视图集处理函数的url配置项
# from rest_framework.routers import SimpleRouter
# router = SimpleRouter()
from rest_framework.routers import DefaultRouter
router = DefaultRouter()

# 注册视图集
from booktest.views import BookInfoViewSet
router.register('books', BookInfoViewSet, base_name='books')

urlpatterns += router.urls