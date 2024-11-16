from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),  # Ajoute une URL pour l'inscription
]