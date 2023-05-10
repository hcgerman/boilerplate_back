import json

import pytest
from django.urls import reverse

pytestmark = pytest.mark.django_db


def test_token_obtain_pair(client, django_user_model) -> None:
    django_user_model.objects.create_user(
        "lennon", "lennon@thebeatles.com", "johnpassword"
    )
    token_obtain_pair_url = reverse("security:token_obtain_pair")
    response = client.post(
        token_obtain_pair_url,
        data={"username": "lennon@thebeatles.com", "password": "johnpassword"},
    )
    data = json.loads(response.content)
    assert response.status_code == 200
    assert data["refresh"] not in ["", None]
    assert data["access"] not in ["", None]


def test_token_obtain_pair_failed(client, django_user_model) -> None:
    token_obtain_pair_url = reverse("security:token_obtain_pair")
    response = client.post(
        token_obtain_pair_url,
        data={"username": "lennon@thebeatles.com", "password": "johnpassword"},
    )
    data = json.loads(response.content)
    assert response.status_code == 401
    assert not "refresh" in data
    assert not "access" in data
    assert data["detail"] not in ["", None]
