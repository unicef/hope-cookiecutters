from django.contrib.auth.models import Group
from rest_framework import serializers


class GroupSerializer(serializers.HyperlinkedModelSerializer[Group]):
    members = serializers.HyperlinkedIdentityField(
        view_name="group-members",
        lookup_url_kwarg="pk",
    )
    permissions = serializers.HyperlinkedIdentityField(
        view_name="group-permissions",
        lookup_url_kwarg="pk",
    )

    class Meta:
        model = Group
        fields = ["name", "members", "permissions"]


class GroupListSerializer(GroupSerializer):
    class Meta:
        model = Group
        fields = ["name", "url"]
