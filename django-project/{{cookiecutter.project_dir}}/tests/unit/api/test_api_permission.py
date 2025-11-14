import pytest
from django.contrib.auth.models import Permission
from django.urls import reverse
from rest_framework.test import APIClient


@pytest.fixture
def client(admin_user):
    client = APIClient()
    client.force_authenticate(user=admin_user)
    return client


def test_permission_list(client):
    url = reverse("api:permission-list")
    res = client.get(url)
    assert res.status_code == 200
    assert res.json()["count"] > 1


def test_permission_detail(client):
    p = Permission.objects.first()
    url = reverse("api:permission-detail", kwargs={"pk": p.pk})
    res = client.get(url)
    assert res.status_code == 200
