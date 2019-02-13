from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('blog/', include('blog.urls')),
    path('mentee/', include('mentee.urls')),
    path('mentor/', include('mentor.urls')),
    path('author/', include('author.urls')),
]