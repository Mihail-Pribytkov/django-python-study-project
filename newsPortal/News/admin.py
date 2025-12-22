from django.contrib import admin
from .models import News, Category

class NewsAdmin(admin.ModelAdmin):
    list_display = [ 'id', 'category', 'title', 'createdAt', 'updateAt']
    list_display_links = ['title']
    search_fields = ['title', 'content']
    list_filter = ['is_published', 'id']
    list_editable = [ 'category']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']

admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
# Register your models here.
