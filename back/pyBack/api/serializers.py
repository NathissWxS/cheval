from rest_framework import serializers
from .models import Equipement, ChevalierEquipement
from django.shortcuts import get_object_or_404


class EquipementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipement
        fields = ['id', 'nom', 'type', 'disponible']
    
class ChevalierSerializer(serializers.Serializer):
    chevalier = serializers.CharField()
    equipements = serializers.ListField(
        child=serializers.CharField()
    )

class chevalierEquipementSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChevalierEquipement
        fields = ['chevalier', 'equipement']

class ChevalierEquipementsResponse(serializers.Serializer):
    chevalier = serializers.CharField()
    equipements = serializers.ListField(
        child=serializers.CharField()
    )