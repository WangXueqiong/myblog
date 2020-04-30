from django.shortcuts import render
from django.http import HttpResponse

from . import models

def index(request):
    articles = models.Article.objects.all()
    return render(request, 'blog/index.html', {'articles': articles})

def article_page(request,article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'blog/article_page.html', {'article': article})

def edit_page(request):
    return render(request, 'blog/edit_page.html')

def edit_action(request):
    id = request.POST.get('id')
    title = request.POST.get('title')
    content = request.POST.get('content')
    if id == '':
        models.Article.objects.create(title = title, content = content)
    else:
        models.Article.objects.filter(id = id).update(title = title, content = content)
    articles = models.Article.objects.all()
    return render(request, 'blog/index.html', {'articles': articles})

def update_action(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'blog/edit_page.html', {'article': article})