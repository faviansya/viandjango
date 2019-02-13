from django.contrib import admin
from .models import Kontenmentor
# Register your models here.

postkonten = [Kontenmentor,]
admin.site.register(postkonten)