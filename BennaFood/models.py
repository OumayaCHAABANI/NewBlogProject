from django.db import models
from django.contrib.auth.models import User
from datetime import date
# Create your models here.

class Categorie (models.Model):
    nom = models.CharField(max_length=100)
    def __str__(self):
        return self.nom

class Recette (models.Model):
    nom   = models.CharField(max_length=100,default=None)
    ingredients = models.TextField(max_length=500,default='Value')
    etapes = models.TextField(max_length=1000,default='Value')
    image = models.ImageField(upload_to='upload_images',default=None,null=False,blank=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    categorie = models.ForeignKey(Categorie,on_delete=models.CASCADE,default=False)
    
    def __str__(self):
        return self.nom
   
    
class Commentaire(models.Model):
    contenu = models.TextField(default='Commentaire')   
    date = models.DateField(default =date.today)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    recette = models.ForeignKey(Recette,on_delete=models.CASCADE,default=None,null = True,blank = True)
    
    

    def __str__(self):  
        return self.contenu
    