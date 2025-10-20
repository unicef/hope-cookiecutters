import sys
from pathlib import Path
from typing import TYPE_CHECKING

import pytest
from django.contrib.auth import get_user_model

if TYPE_CHECKING:
    from django_webtest import DjangoTestApp
    from django_webtest.pytest_plugin import MixinWithInstanceVariables

    User = get_user_model()

here = Path(__file__).parent
sys.path.insert(0, str(here / "../src"))
sys.path.insert(0, str(here / "_demoapp"))
windows = pytest.mark.skipif(sys.platform != "win32", reason="requires windows")

win32only = pytest.mark.skipif("sys.platform != 'win32'")


def skip_if_django_version(v):
    return pytest.mark.skipif("django.VERSION[:2]>={}".format(v), reason="Skip if django>={}".format(v))


@pytest.fixture
def app(
    django_app_factory: "MixinWithInstanceVariables",
    admin_user: "User",
) -> "DjangoTestApp":
    django_app = django_app_factory(csrf_checks=False)
    django_app.set_user(admin_user)
    django_app._user = admin_user
    return django_app
