from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AnonymousUser
from django.forms.utils import ErrorDict

type AnyUser = AbstractBaseUser | AnonymousUser
JsonType = int | str | bool | list[JsonType] | dict[str, JsonType] | ErrorDict | None
