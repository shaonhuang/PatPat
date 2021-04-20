from django.http import JsonResponse
import json
from comments.models import comments


def dispatcher(request):
    if 'usertype' not in request.session:
        return JsonResponse({
            'ret': 302,
            'msg': '未登录',
            'redirect': '/user/sign.html'},
            status=302)
    # 将请求参数统一放入request 的 params 属性中，方便后续处理

    # GET请求 参数在url中，同过request 对象的 GET属性获取
    if request.method == 'GET':
        request.params = request.GET

    # POST/PUT/DELETE 请求 参数 从 request 对象的 body 属性中获取
    elif request.method in ['POST','PUT','DELETE']:
        # 根据接口，POST/PUT/DELETE 请求的消息体都是 json格式
        request.params = json.loads(request.body)


    # 根据不同的action分派给不同的函数进行处理
    action = request.params['action']
    if action == 'list_comment':
        return listcomments(request)
    elif action == 'add_comment':
        return addcomments(request)
    elif action == 'modify_comment':
        return modifycomments(request)
    elif action == 'del_comment':
        return deletecomments(request)

    else:
        return JsonResponse({'ret': 1, 'msg': '不支持该类型http请求'})


def listcomments(request):
    # 返回一个 QuerySet 对象 ，包含所有的表记录
    qs= comments.objects.values()

    # 将 QuerySet 对象 转化为 list 类型
    # 否则不能 被 转化为 JSON 字符串

    gid = request.GET.get('game_id', None)
    userid = request.session.get('_auth_user_id',None)
    ps = int(request.GET.get('pagesize', 10))
    pn = int(request.GET.get('pagenum', 1))
    lci = request.GET.get('lastcommentindex', None)
    if gid:
        qs = qs.filter(game_id=gid)
    if userid:
        qs = qs.filter(user_id=userid)

    retlist = list(qs)
    if lci:
        retlist = retlist[int(lci):int(lci) + ps]
    else:
        retlist = retlist[(pn - 1) * ps:pn * ps]
    return JsonResponse({'ret': 0, 'retlist': retlist})

    #
    # retStr = ''
    # for game in  qs:
    #     for name,value in game.items():
    #         retStr += f'{name} : {value} | '
    #
    #     # <br> 表示换行
    #     retStr += '<br>'
    #
    # return HttpResponse(retStr)


def addcomments(request):

    info    = request.params['data']

    # 从请求消息中 获取要添加客户的信息
    # 并且插入到数据库中
    # 返回值 就是对应插入记录的对象
    record = comments.objects.create(game_id=info['game_id'] ,
                            user_id=request.session.get('_auth_user_id') ,
                            comment_content=info['comment_content'],
                            comment_date=info['comment_date'],
                            rating=info['rating'])


    return JsonResponse({'ret': 0, 'id':record.comment_id})


def modifycomments(request):
    # 从请求消息中 获取修改客户的信息
    # 找到该客户，并且进行修改操作

    commentid = request.params['id']
    newdata = request.params['newdata']

    try:
        # 根据 id 从数据库中找到相应的客户记录
        comment = comments.objects.get(comment_id=commentid)
    except comments.DoesNotExist:
        return {
            'ret': 1,
            'msg': f'id 为`{commentid}`的评论不存在'
        }

    if comment.user_id != int(request.session.get('_auth_user_id', None)):
        return JsonResponse ({
            'ret': 2,
            'msg': f'没有修改权限'
        })
    else:

        if 'comment_content' in newdata:
            comment.comment_content = newdata['comment_content']
        if 'comment_date' in newdata:
            comment.comment_date = newdata['comment_date']
        if 'rating' in newdata:
            comment.rating = newdata['rating']

        # 注意，一定要执行save才能将修改信息保存到数据库
        comment.save()

        return JsonResponse({'ret': 0})


def deletecomments(request):

    commentid = request.params['id']

    try:
        # 根据 id 从数据库中找到相应的客户记录
        comment = comments.objects.get(comment_id=commentid)
    except comment.DoesNotExist:
        return  {
                'ret': 1,
                'msg': f'id 为`{commentid}`的评论不存在'
        }

    if comment.user_id != int(request.session.get('_auth_user_id', None)):
        return JsonResponse ({
            'ret': 2,
            'msg': f'没有修改权限'
        })
    else:
    # delete 方法就将该记录从数据库中删除了
        comment.delete()

        return JsonResponse({'ret': 0})