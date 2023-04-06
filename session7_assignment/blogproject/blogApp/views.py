from django.shortcuts import render
from .models import Article

# Create your views here.

def new(request):
    return render(request, 'new.html')