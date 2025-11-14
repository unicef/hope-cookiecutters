import django_filters.rest_framework
from django.contrib.auth.models import Group, Permission
from django.http import HttpRequest
from rest_framework.decorators import action
from rest_framework.response import Response

from ...models import User
from ..serializers import GroupListSerializer, PermissionListSerializer, PermissionSerializer, UserListSerializer
from .base import BaseReadOnlyModelViewSet


class PermissionViewSet(BaseReadOnlyModelViewSet):
    queryset = Permission.objects.all()
    serializer_class_list = PermissionListSerializer
    serializer_class = PermissionSerializer
    ordering_fields = ("name",)
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ["name", "group"]

    @action(detail=True, methods=["get"])
    def users(self, request: HttpRequest, pk: str = None) -> Response:
        perm: Permission = self.get_object()
        users = User.objects.filter(groups__permissions=perm).distinct()
        serializer = UserListSerializer(users, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=["get"])
    def groups(self, request: HttpRequest, pk: str = None) -> Response:
        perm: Permission = self.get_object()
        groups = Group.objects.filter(permissions=perm)
        serializer = GroupListSerializer(groups, many=True)
        return Response(serializer.data)
