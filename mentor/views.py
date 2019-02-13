from django.shortcuts import render
from .models import Kontenmentor
# Create your views here.


def mentor(request):
    dbmentor = Kontenmentor.objects.all()
    data = {
        'halamanhome': '/',
        'halamanblog': '/blog',
        'halamanmentor': '/mentor',
        'halamanmentee': '/mentee',
        'halamanauthor': '/author',
        'kontenmentor' : dbmentor,
    }
    return render(request, 'mentor.html', data)
