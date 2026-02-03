from django.conf import settings
from rest_framework_simplejwt.authentication import JWTAuthentication


class CookieJWTAuthentication(JWTAuthentication):
    """Authentification JWT qui lit d'abord le header Authorization,
    puis, si absent, lit le token d'accès depuis le cookie httpOnly.
    """

    def authenticate(self, request):
        # 1) Comportement normal: Authorization: Bearer <token>
        header = self.get_header(request)
        if header is not None:
            return super().authenticate(request)

        # 2) Sinon on essaie de lire le token dans le cookie
        cookie_name = getattr(settings, "JWT_AUTH_COOKIE", "access_token")
        raw_token = request.COOKIES.get(cookie_name)
        if not raw_token:
            return None

        validated_token = self.get_validated_token(raw_token)
        return self.get_user(validated_token), validated_token
