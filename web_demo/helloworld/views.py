from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def first_view_func(request):
    """第一个view视图处理函数"""
    # request: 每个视图函数必须有一个参数（习惯叫做request），用来接收请求对象。
    # TODO: 待办事项
    # 返回响应，即给客户端返回的响应体内容：<h1>hello world</h1>
    return HttpResponse("<h1>hello world</h1>")
