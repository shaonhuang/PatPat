from django.urls import path
from . import models
from user import comment
from . import sign_in_out
urlpatterns=[
    path('comment',comment.dispatcher),
    path('sighin', sign_in_out.signin),
    path('signout', sign_in_out.signout),

]