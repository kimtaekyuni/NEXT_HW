from django.shortcuts import render, redirect
from .models import Post, Comment
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
import boto3
import os
from uuid import uuid4
from blog.models import Posts
from django.shortcuts import render
from datetime import datetime
from django.http import JsonResponse

AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME =os.environ.get("AWS_STORAGE_BUCKET_NAME")

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


def write_task(request):
   get_file = request.FILES.get("get_file")
  
   if get_file:
       uuid_name = uuid4()
       image_datetime = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
       fileobj_key = str(uuid_name) + "_" + image_datetime
      
       s3_client = boto3.client(
           "s3",
           aws_access_key_id = AWS_ACCESS_KEY_ID,
           aws_secret_access_key = AWS_SECRET_ACCESS_KEY,
       )
      
       s3_client.upload_fileobj(
           get_file,
           AWS_STORAGE_BUCKET_NAME,
           fileobj_key,
           ExtraArgs={
               "ContentType": get_file.content_type,
           },
       )
      
       image_url = fileobj_key
       image_src = os.environ.get("AWS_BUCKET_URL")+image_url
       Posts.objects.create(
           file=image_url,
       )
       return render(request, "blog/result.html", {"image_url":image_url,"image_src":image_src})
  
   return render(request, "blog/indexpy.html")


def index(request):
   return render(request, 'blog/indexpy.html')
