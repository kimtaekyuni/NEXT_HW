from django.shortcuts import render, redirect
from .models import Post, Comment
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required

def home(request):
    posts = Post.objects.all()

    return render(request, 'blog/home.html', {'posts' : posts})

@login_required(login_url="/accounts/registration/login/")
def new(request):
    if request.method == "POST":
        new_post = Post.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            author = request.user
        )
        return redirect('blog:detail', new_post.pk)
    
    return render(request, 'blog/new.html')

@login_required(login_url="/accounts/registration/login/")
def detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)

    if request.method == 'POST':
        Comment.objects.create(
            post = post,
            content = request.POST['content'],
            author = request.user
        )
        return redirect('blog:detail', post_pk)
    
    return render(request, 'blog/detail.html', {'post':post})

def update(request, post_pk):
    post = Post.objects.get(pk=post_pk)

    if request.method == 'POST':
        Post.objects.filter(pk=post_pk).update(
            title = request.POST['title'],
            content = request.POST['content'],
        )
        return redirect('blog:detail', post_pk)
    
    return render(request, 'blog/update.html', {'post':post})

def delete(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    post.delete()

    return redirect('blog:home')

def delete_comment(request, post_pk, comment_pk):
    comment = Comment.objects.get(pk = comment_pk)
    comment.delete()
    return redirect('blog:detail', post_pk)



