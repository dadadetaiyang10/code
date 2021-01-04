from rest_framework import serializers


class User(object):
    """用户类"""

    def __init__(self, name, age):
        self.name = name
        self.age = age


class UserSerializer(serializers.Serializer):
    """用户序列化器类"""
    name = serializers.CharField()
    # age = serializers.IntegerField(read_only=True) # 作用于序列化
    # age = serializers.IntegerField(write_only=True) # 作用于反序列化
    age = serializers.IntegerField(required=False, default=60)  # 默认required为True
    addr = serializers.CharField(default="上海浦东新区")


if __name__ == '__main__':
    # 1.1 序列化：创建一个User对象
    user = User(name="smart", age=18)

    # 1.2 序列化：创建序列化器对象，传入被序列化的user对象
    serializer = UserSerializer(instance=user)

    # 1.3 序列化：进行序列化操作，使用data方法获取序列化后的数据
    res = serializer.data
    print(res)

    # # 2.1 反序列化：准备数据
    # req_data = {"name": "laowang"}
    #
    # # 2.2 反序列化：创建序列化器对象，传入被校验的数据
    # serializer = UserSerializer(data=req_data)
    #
    # # 2.3 反序列化：使用is_valid()进行数据校验，成功返回True，失败返回False
    # res = serializer.is_valid()
    #
    # # 2.4 判断
    # if res:
    #     print("校验通过：", serializer.validated_data)
    # else:
    #     print("校验失败：", serializer.errors)
