from django.db import models

class News(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(blank=True)
    createdAt = models.DateTimeField(auto_now_add=True, blank=True)
    updateAt = models.DateTimeField(auto_now=True, blank=True)
    photo = models.ImageField(upload_to='media/%Y/%m/%d', null=True, blank=True)
    is_published = models.BooleanField(default=True)
