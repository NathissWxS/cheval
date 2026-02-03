from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from django.shortcuts import get_object_or_404
from .models import Chevalier, ChevalierEquipement, Equipement
from django.contrib.auth.models import User
from .serializers import (
    ChevalierSerializer,
    EquipementSerializer,
    ChevalierEquipementsResponse,
)

class ListeChevaliers(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        chevaliers = Chevalier.objects.all()
        serializer = ChevalierSerializer(chevaliers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = ChevalierSerializer(data=request.data)
        if serializer.is_valid():
            nom_chevalier = serializer.validated_data['nom']
            equipements_noms = serializer.validated_data.get('equipements', [])
            username = serializer.validated_data.get('nom')
            password = serializer.validated_data.get('password')

            if not password:
                return Response({'error': 'password requis'}, status=status.HTTP_400_BAD_REQUEST)

            chevalier, created = Chevalier.objects.get_or_create(nom=nom_chevalier)
            user = User.objects.create_user(username=username, password=password)
            chevalier.user = user
            chevalier.save(update_fields=['user'])
            
            if(equipements_noms is not None):
                for nom_equipement in equipements_noms:
                    equipement = get_object_or_404(Equipement, nom=nom_equipement)
                    ChevalierEquipement.objects.get_or_create(chevalier=chevalier, equipement=equipement)

            return Response({'message': 'Chevalier et équipements associés créés avec succès.'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, chevalier_id):
        chevalier = get_object_or_404(Chevalier, id=chevalier_id)
        chevalier.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

chevaliers = ListeChevaliers.as_view()
    