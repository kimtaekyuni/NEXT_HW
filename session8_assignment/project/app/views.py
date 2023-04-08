from django.shortcuts import render, redirect
from .models import Post
from datetime import date


# Create your views here.

def new(request):
    if request.method == 'POST':
        new_post = Post.objects.create(
            category = request.POST['category'],      
            title = request.POST['title'],
            content = request.POST['content'],
            deadline = request.POST['deadline'],
        )
        return redirect('detail', new_post.pk)

    return render(request, 'new.html')

def detail(request, post_pk ):
    post = Post.objects.get(pk=post_pk)

    return render(request, 'detail.html', {'post': post})

def update(request, post_pk):
    post = Post.objects.get(pk=post_pk)

    if request.method == 'POST':
        Post.objects.filter(pk=post.pk).update(
            title = request.POST['title'],
            content = request.POST['content']
        )
        return redirect('detail', post_pk)
    
    return render(request, 'update.html', {'post': post})

def delete(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    post.delete()

    return redirect('home')

def whole_list(request):
    posts = Post.objects.all()

    return render(request, 'whole_list.html', { 'posts' : posts })

def list(request, category_name):
    posts = Post.objects.filter(category = category_name)
    post = Post.objects.all()
    order_post = post.order_by('deadline')
    remain_days=[]
    for todo in order_post:
        if todo.deadline : 
            remain_day = (todo.deadline - date.today()).days
            remain_days.append(remain_day)  

    return render(request, 'list.html', {'category_name': category_name, 'posts' : posts, 'remain_days': remain_days})


def home(request):
    posts = Post.objects.all()
    To_do = Post.objects.filter(category = 'To_do')
    To_do_len = len(To_do)

    return render(request, 'home.html', { 'posts' : posts, 'To_do_len': To_do_len})

