from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.urls import path

from News.views import HomeNews, NewsByCategory, ViewNews, add_news
# from News.views import HomeNews, get_category, view_news, add_news

urlpatterns = [
    # path('', index, name='Home'),
    # path('category/<int:category_id>/', get_category, name='Category'),
    # path('news/<int:news_id>/', view_news, name='view_news'),

    path('', HomeNews.as_view(), name='Home'),
    path('category/<int:category_id>/', NewsByCategory.as_view(), name='Category'),
    path('news/<int:pk>/', ViewNews.as_view(), name='view_news'),
    path('news/add_news', add_news, name='add_news'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
