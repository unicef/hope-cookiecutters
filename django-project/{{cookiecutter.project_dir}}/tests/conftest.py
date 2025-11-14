import os
import sys
import time
from pathlib import Path

import pytest
from faker import Faker
import responses
from testutils.factories import GroupFactory, UserFactory

faker = Faker()


def pytest_addoption(parser):
    pass


def pytest_configure(config):
    here = Path(__file__).parent
    root = here.parent
    sys.path.insert(0, str(here / "extras"))
    sys.path.insert(0, str(root / "src"))
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{cookiecutter.package_name }}.config.settings")

    from django.conf import settings

    settings.CACHE_PREFIX = str(time.time())
    settings.CSRF_COOKIE_SECURE = False


@pytest.fixture
def mocked_responses():
    with responses.RequestsMock(assert_all_requests_are_fired=False) as rsps:
        yield rsps


@pytest.fixture
def user():
    return UserFactory()


@pytest.fixture
def group():
    return GroupFactory()
