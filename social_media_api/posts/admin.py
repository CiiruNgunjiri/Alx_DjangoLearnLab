# posts/admin.py

from django.contrib import admin
from .models import Post, Like

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'title', 'created_at', 'updated_at')
    search_fields = ('title', 'content')
    list_filter = ('created_at',)

class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'post')
    list_filter = ('post',)

admin.site.register(Post, PostAdmin)
admin.site.register(Like, LikeAdmin)
