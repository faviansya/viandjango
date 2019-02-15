from django.shortcuts import render, redirect
from .models import Posting, YoutubeVideo, Comment
from .forms import PostForm, BeritaForm


def home(request):
    dbHome = Posting.objects.filter(statuspublih=True)
    posts = Posting.objects.filter().order_by('-jadwal_publish')[0:3]
    videocontenct = YoutubeVideo.objects.filter(
        statuspublih=True).order_by('-jadwal_publish')[0:3]
    data = {
        'halamanhome': '/',
        'kontenhome': dbHome,
        'terbaru': posts,
        'kontenvideo': videocontenct,
    }
    return render(request, 'home.html', data)


def lengkap(request, blog_id):
    dbHome = Posting.objects.get(pk=blog_id)
    comments = Comment.objects.filter(mainpage=blog_id)
    data = {
        'halamanhome': '/',
        'kontenhome': dbHome,
        'comment': comments,
    }
    return render(request, 'fullpage.html', data)


def beritalengkap(request):
    dbHome = Posting.objects.filter(statuspublih=True)
    data = {
        'halamanhome': '/',
        'kontenberita': dbHome,

    }
    return render(request, 'beritalengkap.html', data)

def tambahcomment(request, blog_id):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('fullpage',blog_id)
    else:
        form = PostForm()
    data = {
        'halamanhome': '/',
        'form': form,
    }
    return render(request, 'formcomment.html', data)

def tambahberita(request):
    if request.method == 'POST':
        form = BeritaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('waiting')
    else:
        form = BeritaForm()
    data = {
        'halamanhome': '/',
        'form': form,
    }
    return render(request, 'tambahberita.html', data)

def WaitingAff(request):
    return render(request, 'Waiting.html')
