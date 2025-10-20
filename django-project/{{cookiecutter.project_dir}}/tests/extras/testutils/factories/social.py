import factory
from social_django.models import Association, Nonce, UserSocialAuth
from .base import AutoRegisterModelFactory
from .auth import UserFactory


class UserSocialAuthFactory(AutoRegisterModelFactory):
    user = factory.SubFactory(UserFactory)
    uid = factory.Sequence(lambda n: "uid%03d" % n)

    class Meta:
        model = UserSocialAuth


class NonceFactory(AutoRegisterModelFactory):
    timestamp = 1

    class Meta:
        model = Nonce


class AssociationFactory(AutoRegisterModelFactory):
    issued = 1
    lifetime = 1

    class Meta:
        model = Association
