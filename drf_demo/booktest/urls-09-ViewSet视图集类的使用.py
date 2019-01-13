from django.conf.urls import url
from booktest import views


urlpatterns = [
    url(r'^books/$', views.BookInfoViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    url(r'^books/(?P<pk>\d+)/', views.BookInfoViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    }))
]