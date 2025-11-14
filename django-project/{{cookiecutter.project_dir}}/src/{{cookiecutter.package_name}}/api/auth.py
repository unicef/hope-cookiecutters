import logging
from typing import TYPE_CHECKING

from rest_framework import authentication
from rest_framework.permissions import DjangoObjectPermissions
from rest_framework.request import Request

from ..models import ApiKey, User

if TYPE_CHECKING:
    from rest_framework.views import APIView
    from django.db.models import Model

logger = logging.getLogger(__name__)


class ApiKeyAuthentication(authentication.TokenAuthentication):
    keyword = "Key"
    model = ApiKey

    def authenticate(self, request: "Request") -> "tuple[User, ApiKey] | None":
        certs: "tuple[User, ApiKey] | None" = super().authenticate(request)
        if certs:
            request.user = certs[0]
            request.api_key = certs[1]  # type: ignore[attr-defined]
            request.perms = request.api_key.get_permissions()  # type: ignore[attr-defined]
        return certs


class ApiPermission(DjangoObjectPermissions):
    perms_map = {
        "GET": ["%(app_label)s.view_%(model_name)s"],
        "OPTIONS": [],
        "HEAD": [],
        "POST": ["%(app_label)s.add_%(model_name)s"],
        "PUT": ["%(app_label)s.change_%(model_name)s"],
        "PATCH": ["%(app_label)s.change_%(model_name)s"],
        "DELETE": ["%(app_label)s.delete_%(model_name)s"],
    }

    def has_permission(self, request: Request, view: "APIView") -> bool:
        u = getattr(request, "user", None)
        if u and request.user.is_superuser:  # type: ignore[union-attr]
            return True
        if hasattr(request, "api_key"):
            queryset = self._queryset(view)
            perms = self.get_required_permissions(str(request.method), queryset.model)
            return any(item in request.perms for item in perms)
        return False

    def has_object_permission(self, request: Request, view: "APIView", obj: "Model") -> bool:
        u = getattr(request, "user", None)
        if u and request.user.is_superuser:  # type: ignore[union-attr]
            return True
        if hasattr(request, "api_key"):
            queryset = self._queryset(view)
            perms = self.get_required_permissions(str(request.method), queryset.model)
            return any(item in request.perms for item in perms)
        return False
