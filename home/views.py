from django.shortcuts import render

# Create your views here.


def home(request):
    urls = {
        'halamanhome': '/',
        'halamanblog': '/blog',
        'halamanmentor': '/mentor',
        'halamanmentee': '/mentee',
        'halamanauthor': '/author',
    }
    return render(request, 'home.html', urls)
