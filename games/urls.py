from django.urls import path

from . import views

urlpatterns = [
    path('000001/', views.showgame1),
    path('', views.showgame),
    path('gamecomment/',views.game_comment),
]