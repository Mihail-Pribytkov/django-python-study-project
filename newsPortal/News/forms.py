from django import forms
from .models import Category

class NewsForm(forms.Form):
    title = forms.CharField(max_length=150, label='Заголовок')
    content = forms.CharField(label='Текст', required=False)
    is_published = forms.BooleanField(label='Публикация', initial=True)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория', empty_label='Выберите категорию')