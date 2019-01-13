from rest_framework import serializers

from booktest.models import BookInfo, HeroInfo


class BookInfoSerializer(serializers.ModelSerializer):
    """图书序列化器类"""
    class Meta:
        # 指定序列化器类对应模型类
        model = BookInfo
        # 指定需要自动生成哪些字段
        # fields = '__all__'
        # fields = ('id', 'btitle', 'bpub_date', 'bread', 'bcomment', 'image')

        # 指定自动生成字段时排除的字段
        exclude = ('bpub_date', )

        # 指定read_only=True的字段
        # read_only_fields = ('id', 'bread', 'bcomment')

        extra_kwargs = {
            'bread': {
                'min_value': 0,
                # 'required': True
                'help_text': '阅读量'
            },
            'bcomment': {
                'min_value': 0,
                # 'required': True
            }
        }


class HeroInfoSerializer(serializers.ModelSerializer):
    # hbook = BookInfoSerializer()

    class Meta:
        model = HeroInfo
        fields = '__all__'
        depth = 1