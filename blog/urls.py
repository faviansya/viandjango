from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.blog, name='bloghome'),
    path('add', views.tambahblog, name='add'),
    path('<int:blog_id>', views.lengkap, name='lengkapsss'),
]
