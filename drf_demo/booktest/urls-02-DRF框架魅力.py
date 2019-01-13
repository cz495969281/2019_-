from django.conf.urls import url
from booktest import views
from rest_framework.routers import DefaultRouter


urlpatterns = [
    # url(r'^books/$', views.BookListView.as_view()),
    # url(r'^books/(?P<pk>\d+)/$', views.BookDetailView.as_view()),
]

router = DefaultRouter()
router.register('books', views.BookInfoViewSet, base_name='books')
urlpatterns += router.urls
