from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from booktest import views


urlpatterns = [
]

router = DefaultRouter()
router.register('books', views.BookInfoViewSet, base_name='books')
urlpatterns += router.urls