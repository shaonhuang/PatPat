from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Gameinfo
from django.http import JsonResponse
import json
from comments.models import comments

def showgame1(request):
    return HttpResponse("下面是系统中所有的订单信息。。。")


def showgame(request):
    qs = Gameinfo.objects.values()

    ph = request.GET.get('game_id', None)
    kw = request.GET.get('keywords', None)
    ps = int(request.GET.get('pagesize', 10))
    pn = int(request.GET.get('pagenum', 1))
    lgd= request.GET.get('lastgameid', None)

    if ph:
        qs = qs.filter(game_id=ph)
    if kw:
        qs = qs.filter(name__contains = kw)

    gameinfo = list(qs)
    if lgd:
        gameinfo = gameinfo[int(lgd):int(lgd)+ps]
    else:
        gameinfo=gameinfo[(pn-1)*ps:pn*ps]
    return JsonResponse({'ret': 0, 'gameinfo': gameinfo})



# Create your models here.
def game_comment(request):
    qs = comments.objects.values()
    ps = int(request.GET.get('pagesize', 10))
    pn = int(request.GET.get('pagenum', 1))
    lci= request.GET.get('lastcommentindex', None)
    # 将 QuerySet 对象 转化为 list 类型
    # 否则不能 被 转化为 JSON 字符串

    gid = request.GET.get('game_id', None)

    if gid:
        qs = qs.filter(game_id=gid)


        retlist = list(qs)
        if lci:
            retlist = retlist[int(lci):int(lci)+ps]
        else:
            retlist = retlist[(pn - 1) * ps:pn * ps]
        return JsonResponse({'ret': 0, 'retlist': retlist})
    else:
        return JsonResponse ({
            'ret': 1,
            'msg': '缺少游戏id'
        })