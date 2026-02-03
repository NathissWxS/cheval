from django.conf import settings
from django.contrib.auth.models import User
from django.db import transaction
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import Chevalier
from .serializers import RegisterSerializer


class CookieTokenObtainPairView(TokenObtainPairView):
    def finalize_response(self, request, response, *args, **kwargs):
        response = super().finalize_response(request, response, *args, **kwargs)

        if response.status_code == 200 and "access" in response.data:
            access = response.data["access"]
            refresh = response.data.get("refresh")

            response.set_cookie(
                settings.JWT_AUTH_COOKIE,
                access,
                max_age=settings.JWT_AUTH_COOKIE_MAX_AGE,
                httponly=settings.JWT_COOKIE_HTTPONLY,
                secure=settings.JWT_COOKIE_SECURE,
                samesite=settings.JWT_COOKIE_SAMESITE,
                path=settings.JWT_COOKIE_PATH,
            )

            if refresh:
                response.set_cookie(
                    settings.JWT_AUTH_REFRESH_COOKIE,
                    refresh,
                    max_age=settings.JWT_AUTH_REFRESH_COOKIE_MAX_AGE,
                    httponly=settings.JWT_COOKIE_HTTPONLY,
                    secure=settings.JWT_COOKIE_SECURE,
                    samesite=settings.JWT_COOKIE_SAMESITE,
                    path=settings.JWT_COOKIE_PATH,
                )

        return response


class CookieTokenRefreshView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        if "refresh" not in request.data:
            refresh_cookie = request.COOKIES.get(settings.JWT_AUTH_REFRESH_COOKIE)
            if refresh_cookie:
                data = request.data.copy()
                data["refresh"] = refresh_cookie
                request._full_data = data
        return super().post(request, *args, **kwargs)

    def finalize_response(self, request, response, *args, **kwargs):
        response = super().finalize_response(request, response, *args, **kwargs)

        if response.status_code == 200 and "access" in response.data:
            access = response.data["access"]
            response.set_cookie(
                settings.JWT_AUTH_COOKIE,
                access,
                max_age=settings.JWT_AUTH_COOKIE_MAX_AGE,
                httponly=settings.JWT_COOKIE_HTTPONLY,
                secure=settings.JWT_COOKIE_SECURE,
                samesite=settings.JWT_COOKIE_SAMESITE,
                path=settings.JWT_COOKIE_PATH,
            )

        return response


class RegisterView(TokenObtainPairView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        username = serializer.validated_data["username"]
        password = serializer.validated_data["password"]
        nom = serializer.validated_data["nom"]

        if User.objects.filter(username=username).exists():
            return Response({"error": "username déjà utilisé"}, status=status.HTTP_400_BAD_REQUEST)
        if Chevalier.objects.filter(nom=nom).exists():
            return Response({"error": "nom déjà utilisé"}, status=status.HTTP_400_BAD_REQUEST)

        with transaction.atomic():
            user = User.objects.create_user(username=username, password=password)
            chevalier = Chevalier.objects.create(nom=nom, user=user)

        token = TokenObtainPairSerializer.get_token(user)
        access = str(token.access_token)
        refresh = str(token)

        response = Response(
            {
                "message": "compte créé",
                "user_id": user.id,
                "chevalier_id": chevalier.id,
            },
            status=status.HTTP_201_CREATED,
        )

        response.set_cookie(
            settings.JWT_AUTH_COOKIE,
            access,
            max_age=settings.JWT_AUTH_COOKIE_MAX_AGE,
            httponly=settings.JWT_COOKIE_HTTPONLY,
            secure=settings.JWT_COOKIE_SECURE,
            samesite=settings.JWT_COOKIE_SAMESITE,
            path=settings.JWT_COOKIE_PATH,
        )
        response.set_cookie(
            settings.JWT_AUTH_REFRESH_COOKIE,
            refresh,
            max_age=settings.JWT_AUTH_REFRESH_COOKIE_MAX_AGE,
            httponly=settings.JWT_COOKIE_HTTPONLY,
            secure=settings.JWT_COOKIE_SECURE,
            samesite=settings.JWT_COOKIE_SAMESITE,
            path=settings.JWT_COOKIE_PATH,
        )

        return response
