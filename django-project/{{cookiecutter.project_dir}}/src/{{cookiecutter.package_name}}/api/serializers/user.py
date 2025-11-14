from natural_keys import NaturalKeyModelSerializer
from rest_framework import serializers

from ...models import User


class UserSerializer(NaturalKeyModelSerializer[User]):
    groups = serializers.HyperlinkedIdentityField(
        view_name="user-groups",
        lookup_url_kwarg="pk",
    )

    class Meta:
        model = User
        fields = ["username", "email", "is_staff", "groups"]


class UserListSerializer(UserSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "is_staff", "url"]
