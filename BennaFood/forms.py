from django import forms
from BennaFood.models import Recette,Categorie,Commentaire

class CommentaireForm(forms.Modelform)
    class Meta: 
            model = Commentaire
            fields = ('contenu',)
