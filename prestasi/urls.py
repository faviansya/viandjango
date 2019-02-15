from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.prestasi, name='prestasi'),
    path('<int:blog_id>', views.lengkapprestasi, name='fullpageprestasi'),
]
