from django.db import models

class News(models.Model):
    title = models.CharField(max_length=150, verbose_name = 'Заголовок')
    content = models.TextField(blank=True, verbose_name = 'Контент')
    createdAt = models.DateTimeField(auto_now_add=True, blank=True, verbose_name = 'Время создания')
    updateAt = models.DateTimeField(auto_now=True, blank=True, verbose_name = 'Время обновления')
    photo = models.ImageField(upload_to='djangoPythonStudyProject/media/testPhoto', null=True, blank=True, verbose_name = 'Фото')
    is_published = models.BooleanField(default=True, verbose_name = 'Публикация')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')

    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'
        ordering = ['-createdAt']

class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name = 'Категория')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']
