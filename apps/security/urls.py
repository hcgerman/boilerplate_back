from django.urls import path, re_path
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView, TokenBlacklistView

from apps.security.api import auth_view
from apps.security.views import TokenObtainPairView

app_name = "security"

urlpatterns = [
    path("v1/security/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("v1/security/token/blacklist/", TokenBlacklistView.as_view(), name='token_blacklist'),
    path(
        "v1/security/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"
    ),
    path("v1/security/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path(
        "v1/security/auth/current_session/",
        auth_view.current_session,
        name="current_session",
    ),
]
