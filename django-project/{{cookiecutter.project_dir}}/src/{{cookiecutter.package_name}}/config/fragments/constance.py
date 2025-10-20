from collections import OrderedDict

from .. import env

CONSTANCE_ADDITIONAL_FIELDS = {
    "write_only_input": [
        "django.forms.fields.CharField",
        {
            "required": False,
            "widget": "{{cookiecutter.package_name}}.utils.constance.WriteOnlyInput",
        },
    ],
}
CONSTANCE_BACKEND = "constance.backends.database.DatabaseBackend"
CONSTANCE_DATABASE_CACHE_BACKEND = env("CONSTANCE_DATABASE_CACHE_BACKEND")
CONSTANCE_CONFIG = OrderedDict(
    {
        "LOGIN_LOCAL": (True, "Enable local accounts login", bool),
        "LOGIN_SSO": (True, "Enable SSO logon", bool),
    }
)
