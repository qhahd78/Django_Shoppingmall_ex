from django.shortcuts import render

# Create your views here.

def home(request) : 
    return render(request, 'home.html')

def create(request) : 
    return render(request, 'create.html')

def detail(request):
    return render(request, 'detail.html')

def update(request):
    return render(request, 'update.html')