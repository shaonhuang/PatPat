from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse



def showarticle(request):

    return render(request,"static/templates/1.html")