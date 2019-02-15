from django.db import models
from datetime import datetime
from datetime import date
from django.utils import timezone
# Create your models here.


class Posting(models.Model):
    namaauthor = models.CharField(max_length=255, default='admin')
    judul = models.CharField(max_length=255)
    deskripsi = models.TextField(max_length=5000)
    gambar = models.ImageField(upload_to='upload')
    jadwal_publish = models.DateTimeField(default=timezone.now)
    statuspublih = models.BooleanField(default=False)

    def __str__(self):
        return self.judul

class YoutubeVideo(models.Model):
    judul = models.CharField(max_length=255)
    videolink = models.TextField(max_length=5000)
    jadwal_publish = models.DateTimeField(default=timezone.now)
    statuspublih = models.BooleanField(default=False)

    def __str__(self):
        return self.judul

class Comment(models.Model):
    Nama = models.CharField(max_length=255)
    komentar = models.TextField(max_length=5000)
    jadwal_publish = models.DateTimeField(default=timezone.now)
    statuspublih = models.BooleanField(default=True)
    mainpage = models.ForeignKey(Posting, on_delete=models.CASCADE)

    def __str__(self):
        return self.komentar + '  S:' + str(self.statuspublih)
