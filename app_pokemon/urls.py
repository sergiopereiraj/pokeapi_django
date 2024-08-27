from django.urls import path
from . import views

urlpatterns = [

    path('pokemon/<str:pokemon_name>/', views.pokemon_view, name='pokemon_view')
]