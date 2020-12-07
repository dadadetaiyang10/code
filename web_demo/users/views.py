from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def register(request):
    """注册view视图函数"""
    if request.method == "GET":
        # 1.使用register.html模版文件，返回响应
        return render(request, "register.html")
    else:
        # 2.获取表单POST提交的用户名和密码
        username = request.POST.get("username")
        password = request.POST.get("password")
        print("用户名：{0} 密码：{1}".format(username, password))
        return HttpResponse("已经进行注册业务处理")
