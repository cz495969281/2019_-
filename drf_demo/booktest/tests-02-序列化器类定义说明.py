import os

# 设置Django运行所依赖的环境变量
if not os.environ.get('DJANGO_SETTINGS_MODULE'):
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "drf_demo.settings")

from rest_framework import serializers


class User(object):
    """用户类"""
    def __init__(self, username, age, gender):
        self.username = username
        self.age = age
        self.gender = gender


class UserSerializer(serializers.Serializer):
    """序列化器类"""
    # 定义序列化器类字段
    # 字段名 = serializers.字段类型(选项参数)
    username = serializers.CharField()
    age = serializers.IntegerField()
    gender = serializers.BooleanField(write_only=True)
    addr = serializers.CharField(default='浦东新区')

# {
#     "username": "smart",
#     "age": 18
# }
if __name__ == "__main__":
    # 创建user对象
    user = User('smart', 18, True)

    # 创建序列化器对象
    serializer = UserSerializer(user)

    print(serializer.data)