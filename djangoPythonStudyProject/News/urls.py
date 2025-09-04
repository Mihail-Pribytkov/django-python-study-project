from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.urls import path

from News.views import index

urlpatterns = [
    path('', index),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
