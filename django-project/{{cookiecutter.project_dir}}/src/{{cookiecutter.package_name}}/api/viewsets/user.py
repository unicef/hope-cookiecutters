import django_filters.rest_framework
from django.http import HttpRequest
from rest_framework.decorators import action
from rest_framework.response import Response

from ...models import User
from ..serializers import GroupListSerializer, UserListSerializer, UserSerializer
from .base import BaseReadOnlyModelViewSet


class UserViewSet(BaseReadOnlyModelViewSet):
    queryset = User.objects.all()
    ordering = ("username",)
    serializer_class = UserSerializer
    serializer_class_list = UserListSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ["username", "is_staff", "is_superuser", "groups"]

    @action(detail=True, methods=["get"])
    def groups(self, request: HttpRequest, pk: str) -> Response:
        user: User = self.get_object()
        serializer = GroupListSerializer(user.groups.all(), many=True, context={"request": request})
        return Response(serializer.data)
