from django.shortcuts import render
from io import BytesIO
from django.views.generic import View
# from .captcha1 import veri_code
from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url
from PIL import Image
from django.http import HttpResponse
import json
from django.http import JsonResponse


def userindex(request):

    return HttpResponse("下面是系统中所有的订单信息。。。")


# def captcha_img(request):
#     stream = BytesIO()
#     img, code = veri_code()
#     img.save(stream, 'PNG')
#     #看验证码，测试用
#     #img.show()
#     request.session['check_code'] = code
#     return HttpResponse(stream.getvalue())

def captcha():

    hashkey = CaptchaStore.generate_key() # 验证码答案
    image_url = captcha_image_url(hashkey) # 验证码地址
    captcha = {'hashkey': hashkey, 'image_url': image_url}
    return captcha
#刷新验证码
def refresh_captcha(request):
    return HttpResponse(json.dumps(captcha()), content_type='application/json')
# 验证验证码
def jarge_captcha(captchaStr, captchaHashkey):

    if captchaStr and captchaHashkey:
        try:
            # 获取根据hashkey获取数据库中的response值
            get_captcha = CaptchaStore.objects.get(hashkey=captchaHashkey)
            if get_captcha.response == captchaStr.lower():     # 如果验证码匹配
                return True
        except:
            return False
    else:
        return False


def captchaimg(request):
    # stream = BytesIO()
    d=captcha()
    #code=d.get('hashkey')
    #imgurl = d.get('image_url')
    #print(code)
    #print(imgurl)
    # img=Image.open(imgurl)
    # img.save(stream, 'PNG')
    # #看验证码，测试用
    # img.show()
    #
    # request.session['check_code'] = code
    return JsonResponse (d)


