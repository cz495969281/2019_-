import json
from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse, HttpResponse

from booktest.models import BookInfo
# Create your views here.

# 使用Django知识自定义RestAPI接口:
# 1. 获取所有图书信息 GET /books/
# 2. 新建一本图书信息  POST /books/

# 3. 获取指定的图书信息 GET /books/(?P<pk>\d+)/
# 4. 修改指定的图书信息 PUT /books/(?P<pk>\d+)/
# 5. 删除指定的图书信息 DELETE /books/(?P<pk>\d+)/


# /books/
class BookListView(View):
    def get(self, request):
        """获取所有图书信息"""
        # 查询出所有图书信息
        books = BookInfo.objects.all() # QuerySet(查询集)

        # 返回所有图书信息
        books_li = []
        for book in books:
            data = {
                'id': book.id,
                'btitle': book.btitle,
                'bpub_date': book.bpub_date,
                'bread': book.bread,
                'bcomment': book.bcomment,
                'image': book.image.url if book.image else ''
            }

            books_li.append(data)

        # return json
        return JsonResponse(books_li, safe=False)

    def post(self, request):
        """新建一本图书信息"""
        # 前端传递参数时，使用json传递
        # 获取参数(btitle, bpub_date)并进行参数校验
        req_data = request.body # bytes

        # 将bytes->str
        req_data = req_data.decode()

        # 将json字符串-> python字典
        req_dict = json.loads(req_data)

        btitle = req_dict.get('btitle')
        bpub_date = req_dict.get('bpub_date')

        # TODO: 省略参数校验过程...

        # 新增图书信息
        book = BookInfo.objects.create(
            btitle=btitle,
            bpub_date=bpub_date
        )

        # 返回响应: status: 201，包含新建图书的信息
        data = {
            'id': book.id,
            'btitle': book.btitle,
            'bpub_date': book.bpub_date,
            'bread': book.bread,
            'bcomment': book.bcomment,
            'image': book.image.url if book.image else ''
        }

        return JsonResponse(data, status=201)


# /books/(?P<pk>\d+)/
# /books/10/
class BookDetailView(View):
    def get(self, request, pk):
        """获取指定的图书信息"""
        # 根据pk查询指定图书信息
        try:
            book = BookInfo.objects.get(pk=pk)
        except BookInfo.DoesNotExist:
            return HttpResponse(status=404)

        # 返回响应数据
        data = {
            'id': book.id,
            'btitle': book.btitle,
            'bpub_date': book.bpub_date,
            'bread': book.bread,
            'bcomment': book.bcomment,
            'image': book.image.url if book.image else ''
        }

        return JsonResponse(data)

    def put(self, request, pk):
        """修改指定的图书信息"""
        # 根据pk查询指定图书
        try:
            book = BookInfo.objects.get(pk=pk)
        except BookInfo.DoesNotExist:
            return HttpResponse(status=404)

        # 前端传递参数时，使用json传递
        # 获取参数(btitle, bpub_date)并进行参数校验
        req_data = request.body  # bytes

        # 将bytes->str
        req_data = req_data.decode()

        # 将json字符串-> python字典
        req_dict = json.loads(req_data)

        btitle = req_dict.get('btitle')
        bpub_date = req_dict.get('bpub_date')

        # TODO: 省略参数校验过程...

        # 更新图书的信息
        book.btitle = btitle
        book.bpub_date = bpub_date
        book.save()

        # 返回响应数据
        data = {
            'id': book.id,
            'btitle': book.btitle,
            'bpub_date': book.bpub_date,
            'bread': book.bread,
            'bcomment': book.bcomment,
            'image': book.image.url if book.image else ''
        }

        return JsonResponse(data)

    def delete(self, request, pk):
        """删除指定的图书信息"""
        # 根据pk查询指定图书
        try:
            book = BookInfo.objects.get(pk=pk)
        except BookInfo.DoesNotExist:
            return HttpResponse(status=404)

        # 删除图书
        book.delete()

        # 返回响应数据 status: 204
        return HttpResponse(status=204)

