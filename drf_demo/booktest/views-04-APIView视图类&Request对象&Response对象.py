from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.views import View
from django.http import HttpResponse, Http404

# 可以携带请求体数据的请求方式:
# POST
# PUT
# PATCH
# DELETE


# /goods/(?P<pk>\d+)/
# class GoodsView(View):
class GoodsView(APIView):
    def post(self, request, pk):
        """
        self.kwargs: 保存的是从url地址中提取的所有命名参数
        request: request对象是DRF框架中Request类的实例对象，是把Django原始HttpRequest(WSGIRequest)对象做了一层封装
        request.data:
            包含客户端发送请求体数据(表单数据或json数据)，
            原始Django request对象通过request.POST和request.body，
            并且已经转成的字典(dict, OrderedDict, QueryDict)
        request.query_params:
            包含查询字符串的数据，相当原始Django request对象request.GET
            并且已经转成的字典(dict, OrderedDict, QueryDict)

        APIView会对一些异常进行自动的处理，并给客户端返回对应的出错响应信息

        视图返回Response对象，会自动根据前端需要转换为对应的数据类型并返回，仅支持json和html
        前端需要的数据类型通过请求头`Accept`指定，默认返回json
        """
        # raise Http404

        return Response({'name': 'itcast'}, status=status.HTTP_201_CREATED)