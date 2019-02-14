from django.shortcuts import render

# Create your views here.


def home(request):
    urls = {
        'halamanhome': '/',
        'toko': '/toko',
    }
    return render(request, 'homes.html', urls)
