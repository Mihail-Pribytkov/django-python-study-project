from django.shortcuts import render, get_object_or_404, redirect
from .models import News, Category
from .forms import NewsForm
from .utils import MyMixin
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator

class HomeNews(ListView, MyMixin):
    model = News
    context_object_name = 'news'
    template_name = 'News/home_news_list.html'
    extra_context = {'title': 'Главная'}
    mixin_group = 'hello'
    paginate_by = 2

    def get_context_data(self, *, object_list=None,**kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_upper('Главная страница')
        context['mixin_group'] = self.get_prop()
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True).select_related('category')


class NewsByCategory(ListView, MyMixin):
    model = News
    template_name = 'News/home_news_list.html'
    context_object_name = 'news'
    allow_empty = False
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        # Вместо try-except используйте get_object_or_404
        from django.shortcuts import get_object_or_404
        from .models import Category  # Импортируйте Category, а не News_category

        category = get_object_or_404(Category, pk=self.kwargs['category_id'])
        context['title'] = category.title
        context['category'] = category
        return context

    def get_queryset(self):
        return News.objects.filter(
            category_id=self.kwargs['category_id'],
            is_published=True
        ).select_related('category')

class ViewNews(DetailView):
    model = News
    context_object_name = 'news_item'
    template_name = 'News/view_news.html'

class AddNews(CreateView):
    form_class = NewsForm
    template_name = 'News/add_news.html'
    login_url = '/admin/'