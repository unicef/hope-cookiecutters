from typing import TYPE_CHECKING, TypedDict

import pytest
from django.urls import ResolverMatch, resolve
from rest_framework import status
from rest_framework.test import APIClient
from testutils.factories import ApiKeyFactory, GroupFactory, UserFactory
from testutils.perms import group_grant_permissions

if TYPE_CHECKING:
    from django.contrib.auth.models import Group

    from {{cookiecutter.package_name}}.models import (
        ApiKey,
        User,
    )

    Context = TypedDict("Context", {"group": Group, "user": User, "admin": User, "key": ApiKey})

pytestmark = [pytest.mark.api, pytest.mark.django_db]


@pytest.fixture
def client(data: "Context") -> APIClient:
    c = APIClient()
    c._key = data["key"]
    c.credentials(HTTP_AUTHORIZATION=f"Key {c._key.key}")
    return c


@pytest.fixture
def data(admin_user: "User") -> "Context":
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


def pytest_generate_tests(metafunc: pytest.Metafunc) -> None:
    if "url" in metafunc.fixturenames:
        m = []
        ids = []
        for url in [
            "/api/user/",
            "/api/user/{user_pk}/",  # users
            "/api/user/{user_pk}/groups/",
            "/api/group/",
            "/api/group/{group_pk}/",  # users
            "/api/group/{group_pk}/members/",
            "/api/group/{group_pk}/permissions/",
        ]:
            m.append(url)
            r: ResolverMatch = resolve(url)
            ids.append(r.func.__name__)
        metafunc.parametrize("url", m, ids=ids)


def test_urls(client: APIClient, data: "Context", url: str) -> None:
    with group_grant_permissions(
        data["group"],
        [
            "{{cookiecutter.package_name}}.view_user",
            "auth.view_group",
            "auth.view_permission",
        ],
    ):
        url = url.format(user_pk=data["user"].pk, group_pk=data["group"].pk)
        res = client.get(url)
    assert res.status_code == status.HTTP_200_OK, url
