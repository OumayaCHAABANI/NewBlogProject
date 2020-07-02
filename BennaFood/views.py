from django.shortcuts import render,redirect
from BennaFood.models import Recette,Categorie
from django.contrib import messages
from django.contrib.auth.models import User
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa




# Create your views here.
def index(request):
    recette =  Recette.objects.all()
    
    return render(request,'index.html',{'recette':recette})

def about(request):
    return render(request,'about.html') 

def recipes(request):
    recette =  Recette.objects.all()
    return render(request,'recipes.html',{'recette':recette}) 

def singleB(request,id):
    recette=Recette.objects.get(id=id)
    return render(request,'blog_single.html',{"recette":recette})  
    

def profil(request):
    return render(request,'profil.html',{"recettes":Recette.objects.all().filter(user=request.user)}) 

def ModifierProfil(request,id):
    nom= request.POST.get('nom')
    mdp= request.POST.get('mdp')
    confirmmdp= request.POST.get('confirmmdp')
    if(nom == ''):
        messages.error(request,'Nom vide')
    if(mdp== '' or confirmmdp ==''):
            messages.error(request,'Mot de passe vide')
        
    if(mdp != confirmmdp):
        messages.error(request,'Vérifiez le mot de passe')
    
    User.objects.filter(id=id).update(username=nom,password=mdp)        


    return redirect('profil')


       


def ajouter(request):
     if request.method=='POST':
        titre=request.POST['test']
        return  titre
        
def ajoutRecette(request):
    nom=request.POST.get('nom')
    if(nom!=""):
        categories= request.POST.get('categorie')
        if (categories=="sucrés"):
            categorie=Categorie.objects.get(id=1)
        else :
            if(categories=="salés"):
                categorie=Categorie.objects.get(id=2)
            else:
                categorie=Categorie.objects.get(id=3)

        image= request.POST.get('image')
        ingredients= request.POST.get('ingredient')
        etapes= request.POST.get('prepation')
       
        Recette.objects.create(nom=nom,user=request.user,categorie=categorie,ingredients=ingredients,etapes=etapes,image=image)
        
    else :   
        messages.error(request,'Champ vide')
    return redirect('profil')
    
def getpdfPage(request,id):
    recette=Recette.objects.get(id=id)
    data={"recette":recette}
    template=get_template("RecettePdf.html")
    data_p=template.render(data)
    response=BytesIO()
    pdfPage=pisa.pisaDocument(BytesIO(data_p.encode("UTF-8")),response)
    return HttpResponse(response.getvalue(), content_type='application/pdf')
    


def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    context = Context(context_dict)
    html  = template.render(context)
    result = StringIO.StringIO()

    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))

def myview(request):
    #Retrieve data or whatever you need
    return render_to_pdf(
            'profil.html',
            {
                'pagesize':'A4',
                'mylist': results,
            }
        )

def modifierRecette(request,id) :
    nom=request.POST.get('nom')
    image= request.POST.get('image')
    ingredients= request.POST.get('ingredient')
    etapes= request.POST.get('prepation')
       
    if(nom!=""  ):
        categories= request.POST.get('categorie')
        if (categories=="sucrés"):
            categorie=Categorie.objects.get(id=1)
        else :
            if(categories=="salés"):
                categorie=Categorie.objects.get(id=2)
            else:
                categorie=Categorie.objects.get(id=3)

        
    Recette.objects.filter(id=id).update(nom=nom,user=request.user,categorie=categorie,ingredients=ingredients,etapes=etapes,image=image)        
    return redirect('profil')     

def supprimerRecette(request,id):
    Recette.objects.filter(id=id).delete()
    return redirect('profil')
