import re
from django.shortcuts import render, redirect
from .models import Article
import datetime

# Create your views here.
def new(request):
    if request.method == 'POST':
        # POST 요청으로 온 데이터 확인
        print(request.POST)
        # 데이터가 잘 왔나 확인하기 위해 프린트 한 번 해 봄.
        Article.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            category = request.POST['category']
        )
        return redirect('list')

    return render(request, 'new.html')

def list(request):
    len_hobby = len(Article.objects.filter(category='hobby'))
    len_food = len(Article.objects.filter(category='food'))
    len_programming = len(Article.objects.filter(category='programming'))
    ctx = {
        'len_hobby': len_hobby,
        'len_food' : len_food,
        'len_programming': len_programming,
    }
    return render(request, 'list.html', ctx)

def category(request, category_name):
    articles = Article.objects.filter(category=category_name)
    ctx = {
        'articles': articles,
    }
    return render(request, 'category.html', ctx)

def detail(request, article_id):
    article = Article.objects.get(id=article_id)
    return render(request, 'detail.html', {'article': article})

