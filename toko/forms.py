from django import forms 
from .models import KontenBlog

class PostForm(forms.ModelForm):
    class Meta:
        model = KontenBlog
        fields = ('gambar', 'judul','harga', 'deskripsi','deskripsi2','deskripsi3','deskripsi4')
