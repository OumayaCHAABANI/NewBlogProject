from django.shortcuts import render,redirect
from BennaFood.models import Recette,Categorie,Commentaire
from django.contrib import messages
from django.contrib.auth.models import User
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa
from .forms import CommentaireForm




# Create your views here.
def index(request):
    recette = Recette.objects.all().filter()
    

    
    return render(request,'index.html',{"recette":recette})

def about(request):
    return render(request,'about.html') 

def recipes(request):
    recette =  Recette.objects.all().filter()
    query = request.GET.get("q")
    if query :
        recette = recette.filter(nom__icontains= query)


    return render(request,'recipes.html',{'recette':recette}) 


def sweetrecipes(request):
    recette =  Recette.objects.filter (categorie = 1)
    query = request.GET.get("q")
    if query :
        recette = recette.filter(nom__icontains= query)
    return render(request,'sweetrecipes.html',{'recette':recette}) 

def saltrecipes(request):
    recette =  Recette.objects.filter (categorie = 2)
    query = request.GET.get("q")
    if query :
        recette = recette.filter(nom__icontains= query)

    return render(request,'saltrecipes.html',{'recette':recette}) 


def drinkrecipes(request):
    recette =  Recette.objects.filter (categorie = 3)
    query = request.GET.get("q")
    if query :
        recette = recette.filter(nom__icontains= query)


    return render(request,'drinkrecipes.html',{'recette':recette}) 



def singleB(request,id):
    recette=Recette.objects.get(id=id)
    commentaires = recette.commentaires.filter(recette = recette).order_by('date').reverse()
    categorie = recette.categorie.nom
    nv_commentaire = None
    user = request.user
    if request.method == 'POST':
        commentaire_form = CommentaireForm(data = request.POST)
        if commentaire_form.is_valid():
            nv_commentaire = commentaire_form.save(commit = False)
            nv_commentaire.recette = recette
            nv_commentaire.user = user
            nv_commentaire.save()
    else : 
        commentaire_form=CommentaireForm()    
     
            
    return render(request,'blog_single.html',{"recette":recette,
    "commentaires":commentaires,"commentaire_form":commentaire_form,"nv_commentaire":nv_commentaire,"categorie":categorie})  
    

def profil(request):
    return render(request,'profil.html',{"recettes":Recette.objects.all().filter(user=request.user)}) 

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
        ingredient= request.POST.get('ingredient')
        prepation= request.POST.get('prepation')
       
        Recette.objects.create(nom=nom,user=request.user,categorie=categorie,ingredient=ingredient,prepation=prepation)
    
    else :   
        messages.error(request,'Champ vide')
    return redirect('profil')
    
def getpdfPage(request):
    recettes=Recette.objects.all()
    data={"recettes":recettes}
    template=get_template("profil.html")
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
               
