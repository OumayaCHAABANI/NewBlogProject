from django.urls import path

from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('recipes',views.recipes,name='recipes'),
    path('profil',views.profil,name='profil'),
    path('ajoutRecette',views.ajoutRecette,name='ajoutRecette'),
    path('blog_single/<int:id>',views.singleB,name='blog_single'),
    path('getpdfPage',views.getpdfPage,name='getpdfPage')
    
]
