import pytest
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken


@pytest.fixture
def user(django_user_model):
    def _user_factory(**kwargs) -> django_user_model:
        username = kwargs.pop("username", "lennon")
        email = kwargs.pop("email", "lennon@thebeatles.com")
        password = kwargs.pop("password", "johnpassword")
        return django_user_model.objects.create(
            username=username, email=email, password=password, **kwargs
        )

    return _user_factory


@pytest.fixture
def api_client(user):
    default_user = user()
    client = APIClient()
    refresh = RefreshToken.for_user(default_user)
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")

    return client
