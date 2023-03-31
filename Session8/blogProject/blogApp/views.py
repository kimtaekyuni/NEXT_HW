from django.shortcuts import render, redirect
from .models import Article

# Create your views here.

# Article.objects.create(title = "세션하는 날", content="나 천재인가? 이걸 이렇게 잘할 수 있다니")


# Article.objects.all()

# Article.objects.get(pk = 2)

def new(request):
    if request.method == "POST":
    
        print(request.POST)

        new_article = Article.objects.create(
            title = request.POST['title'],
            content = request.POST['content']
        )
        return redirect('list')

    return render(request, 'new.html')

def list(request):
    articles = Article.objects.all()
    return render(request, 'list.html', {'articles': articles})

def detail(request, article_id):
    show_detail = Article.objects.get(pk = article_id)
    return render(request, 'detail.html', {'article': show_detail})