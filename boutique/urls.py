from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('catalogue/', views.catalogue, name='catalogue'),
    path('produit/<int:pk>/', views.produit_detail, name='produit_detail'),
    path('contact/', views.contact, name='contact'),
]
