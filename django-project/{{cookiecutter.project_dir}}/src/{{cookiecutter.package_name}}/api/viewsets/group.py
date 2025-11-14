import django_filters.rest_framework
from django.contrib.auth.models import Group
from django.http import HttpRequest
from rest_framework.decorators import action
from rest_framework.response import Response

from ..auth import ApiPermission
from ..serializers import GroupSerializer, PermissionSerializer, UserListSerializer
from .base import BaseReadOnlyModelViewSet


class GroupViewSet(BaseReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    ordering_fields = ("name",)
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ["name"]

    @action(detail=True, methods=["get"], permission_classes=[ApiPermission])
    def members(self, request: HttpRequest, pk: str) -> Response:
        group: Group = self.get_object()
        serializer = UserListSerializer(group.user_set.all(), many=True, context={"request": request})  # type: ignore[attr-defined]
        return Response(serializer.data)

    @action(detail=True, methods=["get"])
    def permissions(self, request: HttpRequest, pk: str) -> Response:
        group: Group = self.get_object()
        serializer = PermissionSerializer(group.permissions.all(), many=True, context={"request": request})
        return Response(serializer.data)
