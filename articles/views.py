from django.shortcuts import render
from django.http import JsonResponse
from.models import collectiona
# Create your views here.
from django.http import HttpResponse



def showarticle(request,index):

    return render(request,"static/templates/"+str(index)+".html")

def showcollections(request):
    if 'usertype' not in request.session:
        return JsonResponse({
            'ret': 302,
            'msg': '未登录',
            'redirect': '/user/sign.html'},
            status=302)


    qs = collectiona.objects.values()
    userid = request.session.get('_auth_user_id', None)
    ps = int(request.GET.get('pagesize', 10))
    pn = int(request.GET.get('pagenum', 1))
    lgd = request.GET.get('lastgameid', None)


    qs = qs.filter(user_id=userid)
    collectioninfo = list(qs)
    if lgd:
        collectioninfo = collectioninfo[int(lgd):int(lgd) + ps]
    else:
        collectioninfo = collectioninfo[(pn - 1) * ps:pn * ps]
    urllist=[]
    for i in collectioninfo:
        urllist.append("static/templates/"+str(i["article_id"])+".html")

    return JsonResponse({'ret': 0, 'collectioninfo': collectioninfo, 'urllist':urllist})