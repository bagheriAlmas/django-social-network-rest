from django.contrib import admin
from .models import Post, PostFile, Comment


class PostFileInline(admin.TabularInline):
    model = PostFile
    fields = ['file', ]
    extra = 0


class PostCommentsInline(admin.TabularInline):
    model = Comment
    fields = ['user', 'text', 'is_approved']
    extra = 0


class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ['pk', 'title', 'is_active', 'is_public', 'created_at', 'updated_at']
    inlines = [PostFileInline, PostCommentsInline]


admin.site.register(Post, PostAdmin)
