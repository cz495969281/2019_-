from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.views import exception_handler
from django.http import Http404
from django.db import DatabaseError


# /index/
class IndexView(APIView):
    def get(self, request):
        # raise Http404

        raise DatabaseError

        return Response({'message': 'OK'})