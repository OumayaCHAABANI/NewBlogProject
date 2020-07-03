from django.contrib import admin
from .models import Recette,Categorie,Commentaire
# Register your models here.

admin.site.site_header = "Benna Food Admin"
admin.site.site_title = "Benna Admin Area"
admin.site.index_title = " Welcome to the BennaFood admin area"


admin.site.register(Recette)
admin.site.register(Categorie)
admin.site.register(Commentaire) 

