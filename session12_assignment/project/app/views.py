from django.shortcuts import render, redirect
from .models import Post, Comment, double_Comment
from datetime import date
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/registration/login/')
def new(request):
    if request.method == 'POST':
        new_post = Post.objects.create(
            category = request.POST['category'],      
            title = request.POST['title'],
            content = request.POST['content'],
            deadline = request.POST['deadline'],
            author = request.user,
        )
        return redirect('detail', new_post.pk)

    return render(request, 'new.html')

@login_required(login_url='/registration/login/')
def detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    print(post)    
    if request.method == 'POST':
        content = request.POST['content']
        Comment.objects.create(
            post = post, 
            content = content,
            author = request.user,
        )
        return redirect('detail', post_pk)  

    return render(request, 'detail.html', {'post': post})

def update(request, post_pk):
    post = Post.objects.get(pk=post_pk)

    if request.method == 'POST':
        Post.objects.filter(pk=post.pk).update(
            title = request.POST['title'],
            content = request.POST['content'],
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

def delete_comment(request, post_pk, comment_pk):
   comment = Comment.objects.get(pk=comment_pk)
   comment.delete()
   return redirect('detail',post_pk)

def double_comment(request, post_pk, comment_pk):
   post = Post.objects.get(pk=post_pk)        
        
   if request.method == 'POST':
        comment = Comment.objects.get(pk=comment_pk)
        content = request.POST['content']
        double_Comment.objects.create(
            comment = comment, 
            content = content,
        )
        return redirect('detail',post_pk)

   return render(request, 'detail.html', {'post': post})

def delete_double_comment(request, post_pk, comment_pk, double_comment_pk):
   double_comment = double_Comment.objects.get(pk=double_comment_pk)
   double_comment.delete()
   return redirect('detail',post_pk)

def base(request):
    return render(request, 'base.html')

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        exist_user = User.objects.filter(username=username)

        if exist_user:
            error = "이미 존재하는 유저입니다."
            return render(request, 'registration/signup.html', {"error":error})
        
        new_user = User.objects.create_user(username=username, password=password)
        auth.login(request, new_user, backend = "django.contrib.auth.backends.ModelBackend")

        return redirect('home')
    
    return render(request, 'registration/signup.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user, backend = "django.contrib.auth.backends.ModelBackend")
            return redirect(request.GET.get('next', '/'))
        error = "아이디 또는 비밀번호가 틀립니다. "
        return render(request, 'registration/login.html', {"error":error})
    
    return render(request, 'registration/login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')


