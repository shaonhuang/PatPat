from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Gameinfo


def showgame1(request):
    return HttpResponse("下面是系统中所有的订单信息。。。")


def showgame(request):
    qs = Gameinfo.objects.values()

    ph = request.GET.get('game_id', None)

    if ph:
        qs = qs.filter(game_id=ph)

    retStr = ''
    for game in qs:
        for name,value in game.items():
            retStr += f'{name} : {value} | '

        # <br> 表示换行
        retStr += '<br>'

    return HttpResponse(retStr)

from django.http import JsonResponse
import json
from comments.models import comments

# Create your models here.
def game_comment(request):
    qs = comments.objects.values()

    # 将 QuerySet 对象 转化为 list 类型
    # 否则不能 被 转化为 JSON 字符串

    gid = request.GET.get('game_id', None)

    if gid:
        qs = qs.filter(game_id=gid)


        retlist = list(qs)
        return JsonResponse({'ret': 0, 'retlist': retlist})
    else:
        return JsonResponse ({
            'ret': 1,
            'msg': '缺少游戏id'
        })