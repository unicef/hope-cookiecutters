from django.contrib.auth.models import Permission
from rest_framework import serializers


class PermissionSerializer(serializers.HyperlinkedModelSerializer[Permission]):
    class Meta:
        model = Permission
        fields = ["name", "codename"]


class PermissionListSerializer(PermissionSerializer):
    class Meta:
        model = Permission
        fields = PermissionSerializer.Meta.fields + ["url"]
