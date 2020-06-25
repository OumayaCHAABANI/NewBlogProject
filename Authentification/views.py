from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth


# Create your views here.
def connexion(request):
    
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None: 
            auth.login(request,user)
            return redirect('/')  
        else:
            messages.error(request,'Données invalides.')
            return redirect('connexion')  
    else:
        return render(request,'connexion.html')         


def inscription(request):
    if request.method == 'POST' : 
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if not username or not email or not password1 or not password2:
            messages.error(request,'Champ vide')
            return redirect('inscription') 
        if password1==password2:  
            if User.objects.filter(username=username).exists():
                messages.error(request,'Nom utilisateur déjà utilisé')
                return redirect('inscription') 
            elif User.objects.filter(email= email).exists():
                messages.error(request,'Email déjà utilisé')
                return redirect('inscription')
            else:        
                user=User.objects.create_user(username=username, password=password1, email=email)
                user.save()
        else:
             messages.error(request,'Les mots de passes ne correspondent pas..') 
             return redirect('inscription') 
        return redirect('/')
    else:
        return render(request,'inscription.html')
        messages.info(request,'Veuillez remplir les champs vides') 
def deconnexion(request):
    auth.logout(request)
    return redirect('/')        