from django.urls import path
from .views import (
    Equipments,
)
from .viewsAdmin import (
    chevaliers,
)

urlpatterns = [
    path('equipements', Equipments, name='liste_equipements'),
    path('equipements/delete/<int:equipement_id>', Equipments, name='supprimer_equipement'),
    path('admin/chevaliers', chevaliers, name='liste_chevaliers'),
    path('admin/chevaliers/delete/<int:chevalier_id>', chevaliers, name='supprimer_chevalier'),
]