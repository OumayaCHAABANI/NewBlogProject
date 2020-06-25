from django.contrib import admin
from .models import Recette,Categorie,Commentaire
# Register your models here.
admin.site.register(Recette)
admin.site.register(Categorie)
admin.site.register(Commentaire) 
