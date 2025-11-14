import pytest


def test_wsgi() -> None:
    try:
        from {{cookiecutter.package_name}}.config.wsgi import application
    except ImportError as e:
        pytest.fail(f"Failed to import ASGI application: {e}")
    else:
        assert application.request_class, "application.request_class is missing or Falsy (e.g., None)"


def test_asgi() -> None:
    try:
        from {{cookiecutter.package_name}}.config.asgi import application

    except ImportError as e:
        pytest.fail(str(e))
    else:
        assert application.request_class
