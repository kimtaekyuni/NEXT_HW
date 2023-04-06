from django.shortcuts import render
from .models import Post

# Create your views here.
def home(request):
    posts = Post.objects.all()

    return render(request, 'home.html', {'posts': posts})

def new(request):
    if request.method == "POST":
        Post.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
        )

    return render(request, 'new.html')