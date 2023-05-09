from django.shortcuts import render, redirect
from django.contrib import auth
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    return render(request, 'accounts/home.html')

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        age = request.POST['age']

        alreadyuser = User.objects.filter(username = username)

        if alreadyuser:
            error = "이미 존재하는 유저입니다."
            return render(request, 'accounts/registration/signup.html', {"error":error})
        
        new_user = User.objects.create_user(username = username, password = password)

        Profile.objects.create(
            user = new_user,
            age = age 
        )
        auth.login(request, new_user)

        return redirect('blog:home')
    
    return render(request, 'accounts/registration/signup.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('blog:home')
        error = "다시 로그인 해"
        return render(request, 'accounts/registration/login.html', {'error':error})
    
    return render(request, 'accounts/registration/login.html')

def logout(request):
    auth.logout(request)
    return redirect('blog:home')