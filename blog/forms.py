from django import forms 
from .models import KontenBlog

class PostForm(forms.ModelForm):
    class Meta:
        model = KontenBlog
        fields = ('gambar', 'judul', 'deskripsi')
