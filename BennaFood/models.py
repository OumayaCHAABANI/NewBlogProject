from django.db import models
from django.contrib.auth.models import User
from datetime import date
# Create your models here.

class Categorie (models.Model):
    nom = models.CharField(max_length=100)
    def __str__(self):
        return self.nom
class Commentaire(models.Model):
    contenu = models.TextField(default='Commentaire')   
    date = models.DateField(default =date.today)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    

    def __str__(self):  
        return self.contenu
    
class Recette (models.Model):
    nom   = models.CharField(max_length=100,default=None)
    ingredients = models.TextField(max_length=500,default='Value')
    etapes = models.TextField(max_length=500,default='Value')
    image = models.ImageField(upload_to='upload_images',default=None)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    commentaire = models.ForeignKey(Commentaire,on_delete=models.CASCADE,default=None,null = True)
    categorie = models.ForeignKey(Categorie,on_delete=models.CASCADE,default=False)
    
  
    
