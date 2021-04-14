from django.shortcuts import render
from io import BytesIO
from .captcha1 import veri_code

# Create your views here.
from django.http import HttpResponse



def userindex(request):

    return HttpResponse("下面是系统中所有的订单信息。。。")


def captcha_img(request):
    stream = BytesIO()
    img, code = veri_code()
    img.save(stream, 'PNG')
    #看验证码，测试用
    # img.show()
    request.session['check_code'] = code
    return HttpResponse(stream.getvalue())
