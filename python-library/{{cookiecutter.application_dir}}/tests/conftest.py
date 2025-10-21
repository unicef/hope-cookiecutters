import sys
from pathlib import Path

import pytest


here = Path(__file__).parent
sys.path.insert(0, str(here / "../src"))
sys.path.insert(0, str(here / "_demoapp"))
windows = pytest.mark.skipif(sys.platform != "win32", reason="requires windows")

win32only = pytest.mark.skipif("sys.platform != 'win32'")


def skip_if_django_version(v):
    return pytest.mark.skipif("django.VERSION[:2]>={}".format(v), reason="Skip if django>={}".format(v))
