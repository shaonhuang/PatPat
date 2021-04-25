from django.http import JsonResponse
from . import views
from django.contrib.auth import *
# 认证模块
from django.contrib import auth

# 对应数据库
from django.contrib.auth.models import User

# 登录处理
def registration(request):
    # 从 HTTP POST 请求中获取用户名、密码参数
    check_code = request.POST.get('check_code')
    hashkey = request.POST.get('hashkey')
    #if check_code and check_code.lower() == request.session.get('check_code').lower():
    if views.jarge_captcha(check_code, hashkey):
        userName = request.POST.get('username')
        passWord = request.POST.get('password')

        User.objects.create_user(username=userName,password=passWord)

        return JsonResponse({'ret': 0, 'msg':'注册成功'})



    else:
        return JsonResponse({'ret': 2, 'msg': '验证码错误'})


