from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html') 

def recipes(request):
    return render(request,'recipes.html') 

def profil(request):
    return render(request,'profil.html') 

