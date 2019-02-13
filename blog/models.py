from django.db import models

# Create your models here.

class KontenBlog(models.Model):
    gambar = models.ImageField(upload_to='upload')
    judul = models.CharField(max_length=255)
    deskripsi = models.TextField(max_length=5000, default = '')

    def __str__(self):
        return self.judul