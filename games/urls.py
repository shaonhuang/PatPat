from django.urls import path

from . import views

urlpatterns = [
    path('download/', views.downloadgame),
    path('', views.showgame),
    path('gamecomment/',views.game_comment),
]