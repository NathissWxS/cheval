from django.urls import path
from .views import (
    Equipments,
    chevalier_equipements,
    chevalier_equiper,
    chevalier_desequiper,
)
from .viewsAdmin import (
    chevaliers,
    AdminListeEquipements,
)
from .viewsAuth import RegisterView

urlpatterns = [
    path('equipements', Equipments, name='liste_equipements'),
    path('equipements/delete/<int:equipement_id>', Equipments, name='supprimer_equipement'),
    path('chevalier/equipements', chevalier_equipements, name='chevalier_equipements'),
    path('chevalier/equipements/equiper', chevalier_equiper, name='chevalier_equiper'),
    path('chevalier/equipements/retirer', chevalier_desequiper, name='chevalier_desequiper'),
    path('admin/chevaliers', chevaliers, name='liste_chevaliers'),
    path('admin/chevaliers/delete/<int:chevalier_id>', chevaliers, name='supprimer_chevalier'),
    path('register', RegisterView.as_view(), name='register'),
    path('admin/create/equipements', AdminListeEquipements.as_view(), name='admin_create_equipements'),
    path('admin/delete/equipements/<int:equipement_id>', AdminListeEquipements.as_view(), name='admin_delete_equipements'),
]