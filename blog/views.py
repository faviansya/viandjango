from django.shortcuts import render, redirect
from .models import KontenBlog
from .forms import PostForm
# Create your views here.


def blog(request):
    dbblog = KontenBlog.objects.all()
    data = {
        'halamanhome': '/',
        'halamanblog': '/blog',
        'halamanmentor': '/mentor',
        'halamanmentee': '/mentee',
        'halamanauthor': '/author',
        'addblog': '/blog/add',
        'kontenblog': dbblog,
    }
    return render(request, 'blog.html', data)


def tambahblog(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('bloghome')
    else:
        form = PostForm()
    data = {
        'halamanhome': '/',
        'halamanblog': '/blog',
        'halamanmentor': '/mentor',
        'halamanmentee': '/mentee',
        'halamanauthor': '/author',
        'form': form,
    }
    return render(request, 'tambahblog.html', data)


def lengkap(request, blog_id):
    dbblog = KontenBlog.objects.get(pk=blog_id)
    data = {
        'halamanhome': '/',
        'halamanblog': '/blog',
        'halamanmentor': '/mentor',
        'halamanmentee': '/mentee',
        'halamanauthor': '/author',
        'addblog': '/blog/add',
        'kontenblog': dbblog,
    }
    return render(request, 'lengkap.html', data)
