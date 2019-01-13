from rest_framework import serializers
from booktest.models import BookInfo


# serializers.Serializer
class BookInfoSerializer(serializers.ModelSerializer):
    """序列化器类"""
    class Meta:
        model = BookInfo
        # fields = '__all__'
        fields = ('id', 'btitle', 'bpub_date', 'bread', 'bcomment', 'image')
