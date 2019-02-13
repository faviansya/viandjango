from django.shortcuts import render
from .models import kontenmentee
# Create your views here.


def mentee(request):
    dbmentee = kontenmentee.objects.all()
    data = {
        'halamanhome': '/',
        'halamanblog': '/blog',
        'halamanmentor': '/mentor',
        'halamanmentee': '/mentee',
        'halamanauthor': '/author',
        'kontenmentees' : dbmentee
    }
    return render(request, 'mentee.html', data)
