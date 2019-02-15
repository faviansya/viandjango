from django.contrib import admin
from .models import Posting, YoutubeVideo, Comment
# Register your models here.

postmentee = [Posting,YoutubeVideo,Comment,]
admin.site.register(postmentee)