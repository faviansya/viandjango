from django.shortcuts import render, redirect
from .models import KontenBlog
from .forms import PostForm

# Create your views here.


# def toko(request):
#     urls = {
#         'halamanhome': '/',
#         'toko': '/toko',
#     }
#     return render(request, 'toko.html', urls)

def toko(request):
    barang = KontenBlog.objects.all()
    data = {
        'halamanhome': '/',
        'toko': '/toko',
        'listbarang': barang,
    }
    return render(request, 'toko.html', data)

def tambah(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('toko')
    else:
        form = PostForm()
    data = {
        'halamanhome': '/',
        'toko': '/toko',
        'form': form,
    }
    return render(request, 'tambah.html', data)

def lengkap(request, blog_id):
    barang = KontenBlog.objects.get(pk=blog_id)
    data = {
        'halamanhome': '/',
        'toko': '/toko',
        'kontenblog': barang,
    }
    return render(request, 'lengkap.html', data)