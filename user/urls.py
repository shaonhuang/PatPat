from django.urls import path

from user import comment
from . import sign_in_out
from . import register
urlpatterns=[
    path('comment',comment.dispatcher),
    path('article/zan',comment.dianzan),
    path('article/quxiaozan',comment.quxiaodianzan),
    path('signin', sign_in_out.signin),
    path('signout', sign_in_out.signout),
    path('register', register.registration),

]