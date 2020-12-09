from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from users.models import User


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
        # 注册用户信息数据的保存：
        # create方法返回的是一个User模型对象，对应的是用户表中的注册用户的数据
        user = User.objects.create(username=username, password=password)
        # return HttpResponse("恭喜你注册成功！") # 返回的是HttpResponse类的对象
        # return JsonResponse({"message": "注册成功"}) # 返回的是JsonResponse类的对象
        return redirect("/login/")


def login(request):
    """登录view视图函数"""
    if request.method == "GET":
        # 1.如果是访问登录请求，返回登录页面
        # 从客户端传递的cookie中获取登录用户的username
        username = request.COOKIES.get("username", "")
        return render(request, "login.html", context={"username": username})
    else:
        # 2.如果是登录业务逻辑
        # 2.1 获取username和password
        username = request.POST.get("username")
        password = request.POST.get("password")
        remember = request.POST.get("remember")
        # 2.2 对用户名和密码进行校验
        try:
            # 2.2.1 get方法默认利用查到的数据创建一个对应的模型类对象，并将这个模型对象返回
            user = User.objects.get(username=username, password=password)
        except User.DoesNotExist:
            # 2.2.3 查询失败，会出现"模型类.DoseNotExist"异常
            return JsonResponse({"message": "LOGIN FAILED"})
        else:
            # 2.3.4 查询成功
            response = JsonResponse({"message": "LOGIN SUCCESS"})
            # 判断是否需要记住登录用户名：cookie
            if remember == "true":
                # 设置cookie值和7天有效期
                response.set_cookie("username", username, max_age=7 * 24 * 3600)
        return response
