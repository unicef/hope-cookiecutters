from django.apps import AppConfig


class Config(AppConfig):
    name = "{{cookiecutter.package_name}}"

    def ready(self) -> None:
        from . import checks  # noqa
        from . import handlers  # noqa
        from .utils import flags  # noqa
