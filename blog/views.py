from django.shortcuts import render
from django.http import HttpResponse

from . import models

# 博客主页，查询所有博客内容
def index(request):
    articles = models.Article.objects.all()
    return render(request, 'blog/index.html', {'articles': articles})

# 博客内容页面，查询对应博客id的内容
def article_page(request,article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'blog/article_page.html', {'article': article})

# 新建博客页面
def edit_page(request):
    return render(request, 'blog/edit_page.html')

# 编辑博客页面，点击提交，更新博客内容或者新建博客
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

# 修改博客，获取博客的内容
def update_action(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'blog/edit_page.html', {'article': article})