from django.contrib import admin
from .models import KontenBlog

# Register your models here.
postBarang = [KontenBlog,]
admin.site.register(postBarang)