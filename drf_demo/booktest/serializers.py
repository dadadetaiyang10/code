from rest_framework import serializers


class BookInfoSerializer(serializers.Serializer):
    """图书序列化器类"""
    id = serializers.IntegerField(label="ID", read_only=True)
    btitle = serializers.CharField(label="名称", max_length=20)
    bpub_date = serializers.DateField(label="发布日期")
    bread = serializers.IntegerField(label="阅读量", required=False)
    bcomment = serializers.IntegerField(label="评论量", required=False)
