from django.contrib import admin
from .models import Profile, Post, Comment

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'profile_image')

class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'content', 'created_at')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'content', 'created_at')

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
