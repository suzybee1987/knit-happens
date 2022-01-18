from django.contrib import admin
from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_on', 'author', 'image')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment', 'date_added')


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
