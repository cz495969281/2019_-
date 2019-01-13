from django.conf.urls import url
from booktest import views

urlpatterns = [
    url(r'^goods/(?P<pk>\d+)/$', views.GoodsView.as_view()),
]