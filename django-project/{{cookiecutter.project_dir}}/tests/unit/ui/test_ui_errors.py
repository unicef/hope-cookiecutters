from typing import TYPE_CHECKING

import pytest
from django.urls import reverse

if TYPE_CHECKING:
    from django_webtest import DjangoTestApp
    from django_webtest.pytest_plugin import MixinWithInstanceVariables
    from pytest_django.fixtures import SettingsWrapper


pytestmark = [pytest.mark.django_db]


@pytest.fixture
def app(django_app_factory: "MixinWithInstanceVariables", settings: "SettingsWrapper") -> "DjangoTestApp":
    from testutils.factories import UserFactory

    settings.SUPERUSERS = ["superuser"]
    UserFactory(username="superuser", is_staff=False, is_superuser=False)
    UserFactory(username="user", is_staff=False, is_superuser=False)
    return django_app_factory(csrf_checks=False)


@pytest.mark.parametrize("code", [400, 401, 403, 404, 410, 500])
def test_error_pages(app: "DjangoTestApp", code) -> None:
    url = reverse(f"ui:errors-{code}")
    res = app.get(url, expect_errors=True)
    assert res.status_code == code


def test_error_400(app: "DjangoTestApp") -> None:
    res = app.get("/non-existent-url/", expect_errors=True)
    assert res.status_code == 404
