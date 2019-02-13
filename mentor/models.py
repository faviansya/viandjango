from django.db import models

# Create your models here.

class Kontenmentor(models.Model):
    nama = models.CharField(max_length=255)
    pengalaman = models.CharField(max_length=255)
    komentar = models.TextField(max_length=255)
    gambar = models.ImageField(upload_to='upload')

    def __str__(self):
        return self.nama