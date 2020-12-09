from django.db import models


# Create your models here.
class User(models.Model):
    """用户模型类"""
    username = models.CharField(max_length=20, verbose_name="用户名")
    password = models.CharField(max_length=128, verbose_name="密码")
    mobile = models.CharField(max_length=11, null=True, verbose_name="手机号")
    age = models.IntegerField(default=18, verbose_name="年龄")
    gender = models.BooleanField(default=False, verbose_name="性别")

    class Meta:
        # 指定迁移生成的数据表的名称
        db_table = "tb_users"
        # 模型类的解析说明，相当于注释的作用
        verbose_name = "用户表"
