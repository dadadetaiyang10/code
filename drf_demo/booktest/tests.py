# 设置 Django 运行所依赖的环境变量
import json
import os

if not os.environ.get('DJANGO_SETTINGS_MODULE'):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'drf_demo.settings')

# 让 Django 进行一次初始化
import django

django.setup()

from rest_framework import serializers

from booktest.models import BookInfo, HeroInfo
from booktest.serializers import BookInfoSerializer, HeroInfoSerializer


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


class Goods(object):
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock


class GoodsSerializer(serializers.Serializer):
    """商品序列化器类"""
    name = serializers.CharField(label="名称", max_length=40)
    price = serializers.IntegerField(label="价格", max_value=10000, required=False)
    stock = serializers.IntegerField(label="库存", max_value=99999, required=False)


if __name__ == '__main__':
    # # 1.1 序列化：创建一个User对象
    # user = User(name="smart", age=18)
    #
    # # 1.2 序列化：创建序列化器对象，传入被序列化的user对象
    # serializer = UserSerializer(instance=user)
    #
    # # 1.3 序列化：进行序列化操作，使用data方法获取序列化后的数据
    # res = serializer.data
    # print(res)

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

    # # 3.1 序列化单个对象：查询并获取id为1的图书对象
    # book = BookInfo.objects.get(id=1)
    #
    # # 3.2 序列化单个对象：创建序列化器对象
    # serializer = BookInfoSerializer(instance=book)
    #
    # # 3.3 序列化单个对象：进行序列化，获取序列化后的数据
    # res = serializer.data
    # res = json.dumps(res, indent=1, ensure_ascii=False)
    # print(res)

    # # 4.1 查询并获取所有图书数据
    # book = BookInfo.objects.all()
    #
    # # 4.2 创建序列化器对象
    # serializer = BookInfoSerializer(instance=book, many=True)
    #
    # # 4.3 进行序列化，获取序列化之后的数据
    # res = serializer.data
    # res = json.dumps(res, indent=1, ensure_ascii=False)
    # print(res)

    # 2021.1.4作业1：序列化
    # goods = Goods(name="华为", price=4900, stock=1000)
    # serializer = GoodsSerializer(instance=goods)
    # res = serializer.data
    # res = json.dumps(res, indent=1, ensure_ascii=False)
    # print(res)

    # 2021.1.4作业2：反序列化
    # req_data = {'name': '小米10', 'price': 4300}
    # serializer = GoodsSerializer(data=req_data)
    # res = serializer.is_valid()
    # if res:
    #     print("校验通过：", serializer.validated_data)
    # else:
    #     print("校验失败：", serializer.errors)

    # 5.英雄序列化器类
    hero = HeroInfo.objects.get(id=6)
    serializer = HeroInfoSerializer(instance=hero)
    res = serializer.data
    res = json.dumps(res, indent=1, ensure_ascii=False)
    print(res)
