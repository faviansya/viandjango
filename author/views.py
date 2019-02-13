from django.shortcuts import render

# Create your views here.


def author(request):
    urls = {
        'halamanhome': '/',
        'halamanblog': '/blog',
        'halamanmentor': '/mentor',
        'halamanmentee': '/mentee',
        'halamanauthor': '/author',
    }
    return render(request, 'author.html', urls)
