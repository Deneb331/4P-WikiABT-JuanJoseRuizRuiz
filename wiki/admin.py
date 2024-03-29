from django.contrib import admin
from .models import Category, Post, Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}
    list_filter = ('title',)
    list_display = ('title', 'slug')
    search_fields = ('title', 'description')


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('title', )}
    summernote_fields = ('content')
    list_filter = ('status', 'category', 'updated_on')
    list_display = ('title', 'category', 'slug', 'status', 'updated_on')
    search_fields = ('title', 'content')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_filter = ('name', 'approved', 'post')
    list_display = ('name', 'approved', 'post')
    search_fields = ('name', 'post')
