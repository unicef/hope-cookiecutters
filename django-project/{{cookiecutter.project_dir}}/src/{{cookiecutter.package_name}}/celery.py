import os

import celery
from django.conf import settings


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{cookiecutter.package_name}}.config.settings")

app = celery.Celery(
    "{{cookiecutter.package_name}}",
    loglevel="error",
    broker=settings.CELERY_BROKER_URL,
)
app.config_from_object("django.conf:settings", namespace="CELERY", force=True)
