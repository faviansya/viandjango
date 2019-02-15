from django.contrib import admin
from .models import PostingPrestasi
# Register your models here.

postmentee = [PostingPrestasi,]
admin.site.register(postmentee)