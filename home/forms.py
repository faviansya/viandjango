from django import forms 
from .models import Comment,Posting

class PostForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('Nama', 'komentar','mainpage')

class BeritaForm(forms.ModelForm):
    class Meta:
        model = Posting
        fields = ('namaauthor', 'judul','deskripsi', 'gambar')