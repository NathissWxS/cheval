from rest_framework import serializers
from .models import Equipement, ChevalierEquipement, Chevalier
from django.shortcuts import get_object_or_404


class EquipementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipement
        fields = ['id', 'nom', 'type', 'disponible']
    
class ChevalierSerializer(serializers.Serializer):
    user_id = serializers.SerializerMethodField()
    chevalier = serializers.CharField(source='nom')
    password = serializers.CharField(write_only=True, required=False)
    equipements = serializers.ListField(
        child=serializers.CharField(),
        required=False,
    )

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if isinstance(instance, Chevalier):
            data['equipements'] = [e.nom for e in instance.equipement.all()]
        return data

    def get_user_id(self, instance):
        return instance.user.id if instance.user else None

class chevalierEquipementSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChevalierEquipement
        fields = ['chevalier', 'equipement']

class ChevalierEquipementsResponse(serializers.Serializer):
    chevalier = serializers.CharField()
    equipements = serializers.ListField(
        child=serializers.CharField()
    )