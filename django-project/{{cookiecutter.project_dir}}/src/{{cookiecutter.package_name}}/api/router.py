from typing import Any

from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.routers import APIRootView
from rest_framework_extensions.routers import ExtendedDefaultRouter

from . import viewsets as vs


class RootView(APIRootView):
    def get(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        if request.user.is_authenticated:
            return super().get(request, *args, **kwargs)
        return Response({}, status=status.HTTP_401_UNAUTHORIZED)


class ApiRouter(ExtendedDefaultRouter):
    APIRootView = RootView


router = ApiRouter()

(
    router.register(r"user", vs.UserViewSet, basename="user")
    # .register(r"groups", vs.GroupViewSet, basename="user-groups", parents_query_lookups=["user"])
)
(
    router.register(r"group", vs.GroupViewSet, basename="group")
    # .register(r"members", vs.UserViewSet, basename="group-members", parents_query_lookups=["groups"])
    # .register(r"permissions", vs.PermissionViewSet, basename="group-permissions", parents_query_lookups=["group"])
)
(
    router.register(r"permission", vs.PermissionViewSet, basename="permission")
    #     # /permission/{pk}/users/
    #     .register(r"users", vs.UserViewSet, basename="permission-users", parents_query_lookups=["permissions"])
    #     # /permission/{pk}/groups/
    #     .register(r"groups", vs.GroupViewSet, basename="permission-groups", parents_query_lookups=["permissions"])
)
