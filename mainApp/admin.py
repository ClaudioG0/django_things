from django.contrib import admin
from .models import Post

def make_published(modeladmin, request, queryset):
    queryset.update(status='Published')
    make_published.short_description = "Mark posts as published"

def make_drafted(modeladmin, request, queryset):
    queryset.update(status='Draft')
    make_published.short_description = "Mark posts as draft"


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'publish', 'status']
    list_filter = ('status', 'publish')
    search_fields = ('title', 'text')
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')
    actions = [make_published, make_drafted]


