from django.http import HttpResponse

from .models import News

def index(request):
    news = News.objects.all()
    res = '<h1>Список новостей<h1>'
    for i in news:
        res += f'<div>\n<p>{i.title}<p>\n<p>{i.content}<p></div>\n</div>\n<hr>\n'
    return HttpResponse(res)