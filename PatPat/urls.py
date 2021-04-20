"""PatPat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from user.views import userindex, captcha_img
from django.conf import settings
from articles.views import showarticle

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', userindex),
    path('api/games/',include('games.urls')),
    path('api/user/',include('user.urls')),
    path('captcha_img/', captcha_img, name='captcha_img'),
    path('article/', showarticle),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
