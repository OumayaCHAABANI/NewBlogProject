from django import forms
from BennaFood.models import Commentaire

class CommentaireForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = ('contenu','vote',)
        vote = (
            ('','Choisissez une valeur pour la vote'),
            ('1',1),
            ('2',2),
            ('3',3),
            ('4',4),
        )
        widgets = {
            'contenu': forms.TextInput(attrs={'class': 'form-control','name':'message','placeholder':"Saisissez votre message",'rows':'13'}),
            'vote': forms.Select(choices=vote,attrs={'class': 'form-control'})
        }
