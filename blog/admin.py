from django.contrib import admin
from .models import KontenBlog
# Register your models here.

postblog = [KontenBlog,]
admin.site.register(postblog)