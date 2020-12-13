from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View

from users.models import User


def register(request):
    """注册view视图函数"""
    if request.method == "GET":
        # 1.使用register.html模版文件，返回响应
        return render(request, "register.html")
    else:
        # 用loads方法将json格式数据转换为dict字典
        # import json
        # req_dict = json.loads(request.body)

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
    # 判断是否已经登录
    username = request.session.get("username")
    if username:
        # 如果username在session中存在，则表示用户已登录
        return HttpResponse("{0}用户已登录".format(username))

    if request.method == "GET":
        # 1.如果是访问登录请求(get)，返回登录页面
        # (1)从客户端传递的cookie中获取登录用户的username
        # username = request.COOKIES.get("username", "")
        # return render(request, "login.html", context={"username": username})
        # (2)session情况下直接返回html
        return render(request, "login.html")
    else:
        # 2.如果是登录业务逻辑(POST)
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
            # (1)判断是否需要记住登录用户名：cookie
            # response = JsonResponse({"message": "LOGIN SUCCESS"})
            # if remember == "true":
            # (1)设置cookie值和7天有效期
            #     response.set_cookie("username", username, max_age=7 * 24 * 3600)
            # return response

            # (2)添加session记录用户状态的代码
            request.session["user_id"] = user.id
            request.session["username"] = user.username

            # (2)判断是否需要记住登录用户名：session
            if remember != "true":
                # (2)不记住登录，将session的标识cookie设置为：关闭立刻失效
                request.session.set_expiry(0)
            return JsonResponse({"message": "LOGIN SUCCESS"})


def user_info(request, id):
    """获取指定用户的信息"""
    try:
        # 根据id获取指定用户信息
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        # 用户不存在
        return JsonResponse({"message": "用户不存在"})
    else:
        # 用户存在时，通过json返回用户的信息数据
        res_data = {
            "id": user.id,
            "name": user.username,
            "gender": user.gender,
            "age": user.age
        }
        return JsonResponse(res_data)


def is_login(view_func):
    """封装一个装饰器函数判断用户是否登录"""

    def wrapper(request):
        username = request.session.get("username")
        if username:
            # (2)如果username在session中存在，则用户已登录
            return HttpResponse("{0}用户已登录".format(username))
        return view_func(request)

    return wrapper


class LoginView(View):
    """登录类视图"""

    @method_decorator(is_login)
    def get(self, request):
        # 1、获取登录页面
        # (2)判断是否登录
        # response = is_login(request)
        # if response:
        #     return response

        return render(request, "login.html")

    @method_decorator(is_login)
    def post(self, request):
        # 2、登录业务逻辑
        # (2)判断是否登录
        # response = is_login(request)
        # if response:
        #     return response

        # 2.如果是登录业务逻辑(POST)
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
            # (1)判断是否需要记住登录用户名：cookie
            # response = JsonResponse({"message": "LOGIN SUCCESS"})
            # if remember == "true":
            # (1)设置cookie值和7天有效期
            #     response.set_cookie("username", username, max_age=7 * 24 * 3600)
            # return response

            # (2)添加session记录用户状态的代码
            request.session["user_id"] = user.id
            request.session["username"] = user.username

            # (2)判断是否需要记住登录用户名：session
            if remember != "true":
                # (2)不记住登录，将session的标识cookie设置为：关闭立刻失效
                request.session.set_expiry(0)
            return JsonResponse({"message": "LOGIN SUCCESS"})
