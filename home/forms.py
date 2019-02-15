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

    def __init__(self, *args, **kwargs):
        super(BeritaForm, self).__init__(*args, **kwargs)
        self.fields['gambar'].required = False