import factory

from {{cookiecutter.package_name}}.models import ApiKey

from .auth import GroupFactory, UserFactory
from .base import AutoRegisterModelFactory


class ApiKeyFactory(AutoRegisterModelFactory):
    user = factory.SubFactory(UserFactory)
    key = "test-key"
    role = factory.SubFactory(GroupFactory)

    class Meta:
        model = ApiKey
