from django.shortcuts import render, redirect
from .models import Article
from datetime import datetime
# Create your views here.

def new(request):
    if request.method == "POST":
        print(request.POST)

        new_article = Article.objects.create(
            title = request.POST['title'],
            category = request.POST['category'],
            content = request.POST['content'],
            time = datetime.now(),
        )
        return redirect('main')

    return render(request, 'new.html')

def list(request, category_name):
    if category_name == 'main':
        articles = Article.objects.all()
    else:
        articles = Article.objects.filter(category=category_name)

    return render(request, 'list.html', {"category_name":category_name,'articles' : articles})

def detail(request, article_id):
    article = Article.objects.get(id=article_id)
    return render(request, 'detail.html', {'article': article})

def main(request):
    articles = Article.objects.all()
    hobby = Article.objects.filter(category = 'hobby')
    hobby_len = len(hobby)
    food = Article.objects.filter(category = 'food')
    food_len = len(food)
    programming = Article.objects.filter(category = 'programming')
    programming_len = len(programming)
    return render(request, 'main.html', {'articles': articles, 'hobby_len':hobby_len, 'food_len':food_len,'programming_len':programming_len})


