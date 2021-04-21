from django.urls import path
from . import models
from user import comment
from . import sign_in_out
from . import register
urlpatterns=[
    path('comment',comment.dispatcher),
    path('signin', sign_in_out.signin),
    path('signout', sign_in_out.signout),
    path('register', register.registration),

]