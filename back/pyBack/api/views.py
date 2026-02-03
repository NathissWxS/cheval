from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import Equipement, ChevalierEquipement, Chevalier
from .serializers import (
    EquipementSerializer,
    ChevalierEquipementsResponse,
    ChevalierSerializer
)

class ListeEquipements(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        equipements = Equipement.objects.all()
        serializer = EquipementSerializer(equipements, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = EquipementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, equipement_id):
        equipement = get_object_or_404(Equipement, id=equipement_id)
        equipement.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



Equipments = ListeEquipements.as_view()
