from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.toko, name = 'toko'),
    path('tambah', views.tambah, name='tambah'),
    path('<int:blog_id>', views.lengkap, name='lengkapsss'),
]