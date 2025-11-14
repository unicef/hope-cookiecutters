import logging

from django.contrib.auth.models import Group
from django.db import models
from django.db.models.functions import Upper
from django.utils.crypto import RANDOM_STRING_CHARS, get_random_string
from django.utils.translation import gettext_lazy as _

from .base import AbstractModel
from .user import User

logger = logging.getLogger(__name__)

TOKEN_CHARS = f"{RANDOM_STRING_CHARS}-_~."


def make_token() -> str:
    return get_random_string(96, TOKEN_CHARS)


class ApiKey(AbstractModel):
    name = models.CharField(verbose_name=_("Name"), max_length=255, db_collation="und-ci-det")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="keys")
    key = models.CharField(verbose_name=_("Token"), max_length=255, unique=True, default=make_token)
    role = models.ForeignKey(Group, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ("name",)
        unique_together = (("name", "user", "role"),)
        constraints = [models.UniqueConstraint(Upper("name"), "user", name="unique_key_name_for_user")]

    def __str__(self) -> str:
        return self.name

    def get_permissions(self) -> set[str]:
        if self.role:
            return {f"{p.content_type.app_label}.{p.codename}" for p in self.role.permissions.all()}
        return set()
