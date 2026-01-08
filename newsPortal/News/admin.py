from django.contrib import admin
from .models import News, Category
from django.utils.safestring import mark_safe
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class NewsAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = News
        fields = "__all__"

class NewsAdmin(admin.ModelAdmin):
    list_display = [ 'id', 'category', 'title', 'createdAt', 'updateAt', 'get_photo']
    list_display_links = ['title']
    search_fields = ['title', 'content']
    list_filter = ['is_published', 'id']
    list_editable = [ 'category']
    fields = ['title', 'content', 'is_published', 'createdAt', 'updateAt', 'get_photo', 'photo']
    readonly_fields = ('get_photo', 'createdAt', 'updateAt')
    form = NewsAdminForm

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'< img src="{obj.photo.url}" width="100">')
        else:
            return 'Нет фото'

    get_photo_description = 'Миниатюра'

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']

admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.site_title = 'Страница администратора'
admin.site.site_header = 'Страница администратора'
# Register your models here.
