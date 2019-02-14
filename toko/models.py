from django.db import models

# Create your models here.

class KontenBlog(models.Model):
    gambar = models.CharField(max_length=255)
    judul = models.CharField(max_length=255)
    harga = models.CharField(max_length=255)
    deskripsi = models.CharField(max_length=255, blank=True)
    deskripsi2 = models.CharField(max_length=255, blank=True)
    deskripsi3 = models.CharField(max_length=255, blank=True)
    deskripsi4 = models.CharField(max_length=255, blank=True)
    deskripsi5 = models.CharField(max_length=255, blank=True)
    deskripsi6 = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.judul
