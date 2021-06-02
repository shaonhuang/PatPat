from django.urls import path
from django.urls import re_path
from . import views

urlpatterns = [
    path('collections/',views.showcollections),
    re_path(r'^([0-9]{1})/$', views.showarticle),

]