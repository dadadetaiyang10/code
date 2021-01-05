from rest_framework import serializers


class BookInfoSerializer(serializers.Serializer):
    """图书序列化器类"""
    id = serializers.IntegerField(label="ID", read_only=True)
    btitle = serializers.CharField(label="名称", max_length=20)
    bpub_date = serializers.DateField(label="发布日期")
    bread = serializers.IntegerField(label="阅读量", required=False)
    bcomment = serializers.IntegerField(label="评论量", required=False)

    # 关联对象嵌套序列化字段
    # 嵌套序列化方式1：PrimaryKeyRelatedField - 将关联对象序列化为关联对象的主键
    # heroinfo_set = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    # 嵌套序列化方式2：将关联对象使用指定的序列化器进行嵌套序列化
    # heroinfo_set = HeroInfoSerializer(label="英雄")
    # 嵌套序列化方式3：StringRelatedField - 将关联对象序列化为关联对象所属模型类__str__方法的返回值
    heroinfo_set = serializers.StringRelatedField(read_only=True, many=True)


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

    # 嵌套序列化方式1：PrimaryKeyRelatedField - 将关联对象序列化为关联对象的主键
    # hbook = serializers.PrimaryKeyRelatedField(label="图书", read_only=True)
    # 嵌套序列化方式2：将关联对象使用指定的序列化器进行嵌套序列化
    # hbook = BookInfoSerializer(label='图书')
    # 嵌套序列化方式3：StringRelatedField - 将关联对象序列化为关联对象所属模型类__str__方法的返回值
    # hbook = serializers.StringRelatedField(label="图书")
