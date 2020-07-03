from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
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
    
  
    
class Commentaire(models.Model):
    contenu = models.TextField(default=None)   
    date = models.DateTimeField(default=now)
    vote = models.IntegerField(default = 0 , null =True,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    recette = models.ForeignKey(Recette,on_delete=models.CASCADE,default=None,null = True,blank = True,related_name='commentaires')
    active = models.BooleanField(default= False)
    

    def __str__(self):  
        return self.contenu
   
