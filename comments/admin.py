from django.contrib import admin
from .models import comments
from .models import collections
# Register your models here.
admin.site.register(comments)
admin.site.register(collections)