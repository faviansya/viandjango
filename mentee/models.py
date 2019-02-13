from django.db import models

# Create your models here.
class kontenmentee(models.Model):
    nama = models.CharField(max_length=255)
    komentar = models.CharField(max_length=255)
    gambar = models.CharField(max_length=255)

    def __str__(self):
        return self.nama