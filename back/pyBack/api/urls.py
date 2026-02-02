from django.urls import path
from .views import (
    Equipments,
)

urlpatterns = [
    path('equipements', Equipments, name='liste_equipements'),
    path('equipements/<int:equipement_id>', Equipments, name='supprimer_equipement'),
]