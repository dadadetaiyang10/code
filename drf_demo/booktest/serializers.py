from rest_framework import serializers


class BookInfoSerializer(serializers.Serializer):
    """图书序列化器类"""
    id = serializers.IntegerField(label="ID", read_only=True)
    btitle = serializers.CharField(label="名称", max_length=20)
    bpub_date = serializers.DateField(label="发布日期")
    bread = serializers.IntegerField(label="阅读量", required=False)
    bcomment = serializers.IntegerField(label="评论量", required=False)


class HeroInfoSerializer(serializers.Serializer):
    """英雄序列化器类"""
    GENDER_CHOICES = (
        (0, '男'),
        (1, '女')
    )
    id = serializers.IntegerField(label='ID', read_only=True)
    hname = serializers.CharField(label='名字', max_length=20)
    # choices选项参数：和校验有关，用来限定 hgender 的取值范围
    hgender = serializers.ChoiceField(label='性别', choices=GENDER_CHOICES, required=False)
    hcomment = serializers.CharField(label='描述信息', max_length=200, required=False)
