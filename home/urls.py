from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('beritalengkap', views.beritalengkap, name='beritalengkap'),
    path('tambahberita', views.tambahberita, name='tambahberita'),
    path('<int:blog_id>', views.lengkap, name='fullpage'),
    path('<int:blog_id>/comment', views.tambahcomment, name='commentpage'),
    path('waiting', views.WaitingAff, name='waiting'),

]
