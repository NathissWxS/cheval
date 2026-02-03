from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import Equipement, ChevalierEquipement, Chevalier
from .middleware import JWT
from .serializers import (
    EquipementSerializer,
    ChevalierEquipementsResponse,
    ChevalierSerializer
)

class ListeEquipements(APIView):
    # permission_classes = [IsAuthenticated]
    authentication_classes = [JWT]

    def get(self, request):
        equipements = Equipement.objects.all()
        serializer = EquipementSerializer(equipements, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



Equipments = ListeEquipements.as_view()


class ChevalierEquipements(APIView):
    # permission_classes = [IsAuthenticated]
    authentication_classes = [JWT]

    def get(self, request):
        if not hasattr(request.user, "chevalier"):
            return Response({"error": "chevalier introuvable"}, status=status.HTTP_404_NOT_FOUND)

        chevalier = request.user.chevalier
        equipements = chevalier.equipement.all()
        serializer = EquipementSerializer(equipements, many=True)
        return Response(
            {
                "chevalier": chevalier.nom,
                "equipements": serializer.data,
            },
            status=status.HTTP_200_OK,
        )


chevalier_equipements = ChevalierEquipements.as_view()


class ChevalierEquiper(APIView):
    # permission_classes = [IsAuthenticated]
    authentication_classes = [JWT]

    def post(self, request):
        if not hasattr(request.user, "chevalier"):
            return Response({"error": "chevalier introuvable"}, status=status.HTTP_404_NOT_FOUND)

        equipement_id = request.data.get("equipement_id")
        if not equipement_id:
            return Response({"error": "equipement_id requis"}, status=status.HTTP_400_BAD_REQUEST)

        equipement = get_object_or_404(Equipement, id=equipement_id)
        chevalier = request.user.chevalier

        ChevalierEquipement.objects.get_or_create(
            chevalier=chevalier,
            equipement=equipement,
        )

        return Response(
            {"message": "équipement ajouté"},
            status=status.HTTP_201_CREATED,
        )


chevalier_equiper = ChevalierEquiper.as_view()


class ChevalierDesequiper(APIView):
    # permission_classes = [IsAuthenticated]
    authentication_classes = [JWT]

    def delete(self, request):
        if not hasattr(request.user, "chevalier"):
            return Response({"error": "chevalier introuvable"}, status=status.HTTP_404_NOT_FOUND)

        equipement_id = request.data.get("equipement_id")
        if not equipement_id:
            return Response({"error": "equipement_id requis"}, status=status.HTTP_400_BAD_REQUEST)

        chevalier = request.user.chevalier
        association = ChevalierEquipement.objects.filter(
            chevalier=chevalier,
            equipement_id=equipement_id,
        ).first()

        if not association:
            return Response({"error": "équipement non trouvé"}, status=status.HTTP_404_NOT_FOUND)

        association.delete()

        return Response(
            {"message": "équipement retiré"},
            status=status.HTTP_200_OK,
        )

class isConnected(APIView):
    # permission_classes = [IsAuthenticated]
    authentication_classes = [JWT]

    def get(self, request):
        return Response({"message": "utilisateur connecté"}, status=status.HTTP_200_OK)

isConnected = isConnected.as_view()


chevalier_desequiper = ChevalierDesequiper.as_view()
