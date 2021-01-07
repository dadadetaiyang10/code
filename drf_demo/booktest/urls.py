# 设置 Django 运行所依赖的环境变量
import json
import os

if not os.environ.get('DJANGO_SETTINGS_MODULE'):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'drf_demo.settings')

# 让 Django 进行一次初始化
import django

django.setup()

from django.urls import re_path
from rest_framework.routers import SimpleRouter

from booktest import views

# urlpatterns = [
#     re_path(r"^books/$", views.BookInfoViewSet.as_view(
#         {"get": "list", "post": "create"}
#     )),
#     re_path(r"^books/(?P<pk>\d+)/$", views.BookInfoViewSet.as_view(
#         {"get": "retrieve", "put": "update", "delete": "destroy"}
#     )),
#     re_path(r"^books/$", views.BookInfoViewSet.as_view(
#         {"get": "latest"}
#     )),
#     re_path(r"^books/$", views.BookInfoViewSet.as_view(
#         {"put": "read"}
#     )),
# ]

urlpatterns = []
# 1.创建router对象
router = SimpleRouter()

# 2.注册视图集
router.register("books", views.BookInfoViewSet, basename="books")

# 3.添加url配置
urlpatterns += router.urls

# 测试：打印生成的 URL 配置项
for url in router.urls:
    print(url)
