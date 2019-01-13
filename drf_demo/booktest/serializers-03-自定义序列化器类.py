from rest_framework import serializers

from booktest.models import BookInfo


class HeroInfoSerializer(serializers.Serializer):
    """英雄序列化器类"""
    GENDER_CHOICES = (
        (0, '男'),
        (1, '女')
    )

    id = serializers.IntegerField(label='英雄ID', read_only=True)
    hname = serializers.CharField(label='名称', max_length=20)
    hgender = serializers.ChoiceField(label='性别', choices=GENDER_CHOICES)
    hcomment = serializers.CharField(label='备注信息', max_length=200, allow_null=True)

    # 将关联对象序列化为关联对象的主键
    # hbook = serializers.PrimaryKeyRelatedField(label='图书', read_only=True)

    # 使用指定的序列化器将关联对象进行序列化
    # hbook = BookInfoSerializer()

    # 将关联对象序列化对应模型类中__str__方法的返回值
    # hbook = serializers.StringRelatedField(label='图书')


# 自定义数据验证方法
def about_django(value):
    if 'django' not in value.lower():
        raise serializers.ValidationError('图书不是关于Django的')
    return value


class BookInfoSerializer(serializers.Serializer):
    """图书序列化器类"""
    id = serializers.IntegerField(label='图书编号', read_only=True)
    # btitle = serializers.CharField(label='标题', max_length=20, validators=[about_django])
    btitle = serializers.CharField(label='标题', max_length=20)
    bpub_date = serializers.DateField(label='发布日期')
    # bread = serializers.IntegerField(label='阅读量', required=False, default=0)
    bread = serializers.IntegerField(label='阅读量', required=False)
    bcomment = serializers.IntegerField(label='评论量', required=False)
    image = serializers.ImageField(label='图片', required=False)

    # 将关联对象序列化为关联对象的主键，关联对象有多个，指定many=True
    # heroinfo_set = serializers.PrimaryKeyRelatedField(label='英雄', read_only=True, many=True)

    # 使用指定的序列化器将关联对象进行序列化
    # heroinfo_set = HeroInfoSerializer(many=True)

    # 将关联对象序列化对应模型类中__str__方法的返回值
    # heroinfo_set = serializers.StringRelatedField(label='图书', many=True)

    # def validate_btitle(self, value):
    #     """这个方法会对btitle字段的内容进行校验"""
    #     if 'django' not in value.lower():
    #         raise serializers.ValidationError('图书不是关于Django的2')
    #     return value

    # def validate(self, attrs):
    #     """
    #     attrs: 包含传递的data数据的内容的字典
    #     """
    #     # 获取bread和bcomment
    #     bread = attrs['bread']
    #     bcomment = attrs['bcomment']
    #
    #     if bread < bcomment:
    #         raise serializers.ValidationError('阅读量必须大于等于评论量')
    #
    #     return attrs

    def create(self, validated_data):
        """
        validated_data: 校验之后的数据，是一个字典dict
        """
        # print('create方法被调用')
        # print(validated_data)

        book = BookInfo.objects.create(**validated_data)

        return book

    def update(self, instance, validated_data):
        """
        instance: 创建序列化器时传入的对象
        validated_data: 校验之后的数据
        """
        # print('update方法被调用')
        # print(type(instance))
        # print(instance)
        # print(validated_data)

        instance.btitle = validated_data.get('btitle')
        instance.bpub_date = validated_data.get('bpub_date') # None

        # 调用模型对象的save方法表数据更新
        instance.save()

        return instance



