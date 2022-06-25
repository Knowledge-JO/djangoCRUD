from pyexpat import model
from statistics import mode
from django.contrib import admin
from .models import Post
# Register your models here.

class BlogDB(admin.ModelAdmin):
    list_display = [
        "title", "author","slug","status","publish","created"
    ]


admin.site.register(Post, BlogDB)