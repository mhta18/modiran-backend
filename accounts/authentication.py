from rest_framework_simplejwt.authentication import JWTAuthentication


class CookieJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        # اگر درخواست به مسیرهای لاگین یا ثبت‌نام بود، از احراز هویت صرف‌نظر کن
        if "/auth/login/" in request.path or "/auth/register/" in request.path:
            return None

        # دریافت توکن از کوکی HttpOnly
        raw_token = request.COOKIES.get("access_token")

        if raw_token is None:
            return None

        try:
            validated_token = self.get_validated_token(raw_token)
            return self.get_user(validated_token), validated_token
        except Exception:
            return None
