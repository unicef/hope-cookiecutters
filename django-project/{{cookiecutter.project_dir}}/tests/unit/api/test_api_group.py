from typing import TYPE_CHECKING, TypedDict

import pytest
from django.contrib.auth.models import Group
from django.urls import reverse
from rest_framework.test import APIClient
from testutils.perms import group_grant_permissions


if TYPE_CHECKING:
    from {{cookiecutter.package_name}}.models import ApiKey, User

    Context = TypedDict("Context", {"group": Group, "user": User, "admin": User, "key": ApiKey})

pytestmark = [pytest.mark.api, pytest.mark.django_db]


@pytest.fixture
def client(data: "Context"):
    client = APIClient()
    client._key = data["key"]
    client.credentials(HTTP_AUTHORIZATION=f"Key {client._key.key}")
    return client


@pytest.fixture
def data(admin_user: "User") -> "Context":
    from testutils.factories import ApiKeyFactory, GroupFactory, UserFactory

    u: User = UserFactory()
    g: Group = GroupFactory()
    u.groups.add(g)

    key: ApiKey = ApiKeyFactory(user=u, role=g)

    return {
        "group": g,
        "key": key,
        "user": u,
        "admin": admin_user,
    }


def test_user_list(client, data: "Context"):
    group = data["group"]
    url = reverse("api:group-list")
    with group_grant_permissions(group, ["auth.view_group"]):
        res = client.get(url)
    assert res.status_code == 200
    assert res.json()["count"] == 1


def test_user_detail(client, data: "Context"):
    group = data["group"]
    url = reverse("api:group-detail", kwargs={"pk": group.pk})
    with group_grant_permissions(group, ["auth.view_group"]):
        res = client.get(url)
    assert res.status_code == 200
    assert res.json()["name"] == group.name
