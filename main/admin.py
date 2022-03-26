from django.contrib import admin
from .models import BlogTag, BlogCategory, BlogPost


@admin.register(BlogTag)
class BlogTagAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'created',
        'updated',
    )
    list_per_page = 25
    date_hierarchy = 'created'


@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'created',
        'updated',
    )
    list_per_page = 25
    date_hierarchy = 'created'


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'created',
        'updated',
    )
    list_per_page = 25
    date_hierarchy = 'created'
