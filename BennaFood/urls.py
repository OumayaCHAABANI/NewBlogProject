from django.urls import path

from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('recipes',views.recipes,name='recipes'),
    path('profil',views.profil,name='profil'),
    path('ModifierProfil/<int:id>',views.ModifierProfil,name='ModifierProfil'),
    path('ajoutRecette',views.ajoutRecette,name='ajoutRecette'),
    path('blog_single/supprimerRecette/<int:id>',views.supprimerRecette,name='supprimerRecette'),
    path('modifierRecette/<int:id>',views.modifierRecette,name='modifierRecette'),
    path('blog_single/<int:id>',views.singleB,name='blog_single'),
    path('getpdfPage/<int:id>',views.getpdfPage,name='getpdfPage')
    
]
