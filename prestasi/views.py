from django.shortcuts import render
from .models import PostingPrestasi

# Create your views here.


def prestasi(request):
    posts = PostingPrestasi.objects.filter().order_by('-jadwal_publish')[0:3]
    prestasidb = PostingPrestasi.objects.filter(statuspublih=True)
    data = {
        'halamanhome': '/',
        'kontenhome': prestasidb,
        'prestasiterbaru': posts,
    }
    return render(request, 'prestasi.html', data)

def lengkapprestasi(request, blog_id):
    dbHome = PostingPrestasi.objects.get(pk=blog_id)
    data = {
        'halamanhome': '/',
        'kontenprestasi': dbHome,
    }
    return render(request, 'prestasilengkap.html', data)