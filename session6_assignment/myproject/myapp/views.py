from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request, 'main.html')

def photo(request):
    return render(request, 'photo.html')

def Information(request):
    return render(request, 'Information.html')