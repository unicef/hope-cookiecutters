import logging
import os
from pathlib import Path

here = Path(__file__).parent

logger = logging.getLogger(__name__)

ALLOWED_HOSTS = ["*"]
DEBUG = True

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [str(here / "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.contrib.messages.context_processors.messages",
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.request",
            ]
        },
    },
]
DATABASES = {
    "default": {
        # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "DEMODB.sqlite",  # Not used with sqlite3.
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "",
        "PORT": "",  # Set to empty string for default. Not used with sqlite3.
    }
}

SITE_ID = 1
STATIC_URL = "/static/"
SECRET_KEY = "c73*n!y=)tziu^2)y*@5i2^)$8z$tx#b9*_r3i6o1ohxo%*2^a"
MIDDLEWARE = (
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
)

ROOT_URLCONF = "demo.urls"
WSGI_APPLICATION = "demo.wsgi.application"

AUTHENTICATION_BACKENDS = ("demo.backends.AnyUserBackend",)

INSTALLED_APPS = (
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.admin",
    "{{cookiecutter.package_name}}.apps.Config",
    "demo",
)

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
STREAMING = {
    "BROKER_URL": os.environ.get("BROKER_URL", "console://"),
    "MANAGER_CLASS": "streaming.manager.ChangeManager",
    "QUEUES": {
        "default": {
            "binding_keys": ["*"],
        },
        "security": {"binding_keys": ["user.*", "group.*"]},
        "payments": {"binding_keys": ["plan.*"]},
    },
    "DEBUG": True,
}

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {"class": "logging.StreamHandler"},
        "null": {"class": "logging.NullHandler"},
    },
    "root": {
        "handlers": ["null"],
        "level": "CRITICAL",
    },
    "loggers": {
        "django": {"handlers": ["console"], "level": "CRITICAL"},
        "faker": {"handlers": ["null"], "level": "CRITICAL"},
        "pika": {"handlers": ["null"], "level": "DEBUG", "propagate": False},
    },
}
