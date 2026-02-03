from django.conf import settings
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


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
