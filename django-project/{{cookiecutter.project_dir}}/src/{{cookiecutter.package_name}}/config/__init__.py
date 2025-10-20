import os
import tempfile
from smart_env import SmartEnv

DEFAULTS = {
    "CELERY_BROKER_URL": (str, "redis://localhost:6379/2"),
    "CELERY_TASK_ALWAYS_EAGER": (bool, False),
    "CONSTANCE_DATABASE_CACHE_BACKEND": (str, ""),
    "CORS_ALLOWED_ORIGINS": (list, []),
    "CSP_REPORT_ONLY": (bool, False, True),
    "CSRF_COOKIE_NAME": (str, "{{ cookiecutter.package_name }}"),
    "CSRF_COOKIE_SECURE": (bool, True, False),
    "CSRF_TRUSTED_ORIGINS": (list, [], []),
    "DATABASE_URL": (str, 'psql://postgres:@127.0.0.1:5432/"{{ cookiecutter.database_name }}"'),
    "DEBUG": (bool, False),
    "DEVELOPMENT": (bool, False),
    "EMAIL_BACKEND": (str, "django.core.mail.backends.smtp.EmailBackend"),
    "EMAIL_HOST": (str, ""),
    "EMAIL_HOST_PASSWORD": (str, ""),
    "EMAIL_HOST_USER": (str, ""),
    "EMAIL_PORT": (int, ""),
    "EMAIL_USE_TLS": (bool, True),
    "EXTRA_APPS": (list, "", "", False, ""),  # nosec
    "EXTRA_AUTHENTICATION_BACKENDS": (list, [], [], False, "Extra authentications backends enabled to add."),
    "EXTRA_MIDDLEWARES": (list, "", "", False, ""),  # nosec
    "GDAL_LIBRARY_PATH": (str, None),
    "GEOS_LIBRARY_PATH": (str, None),
    "LOGIN_LOCAL": (bool, True),
    "LOGIN_SSO": (bool, True),
    "MEDIA_ROOT": (str, os.path.join(tempfile.gettempdir(), "{{ cookiecutter.package_name }}", "media")),
    "REDIS_CACHE_URL": (str, "redis://localhost:6379/0"),
    "REDIS_LOCK_URL": (str, "redis://localhost:6379/1?backend=django_redis.cache.RedisCache"),
    "REDIS_TSDB_URL": (str, "redis://localhost:6379/2"),
    "SECRET_KEY": (str, ""),
    "SENTRY_DSN": (str, ""),
    "SENTRY_ENABLED": (bool, False),
    "STATIC_ROOT": (str, os.path.join(tempfile.gettempdir(), "{{ cookiecutter.package_name }}", "static")),
    "STREAMING_BROKER_URL": (str, "", ""),
    "TIME_ZONE": (str, "{{ cookiecutter.timezone }}"),
    "URL_PREFIX": (str, ""),
}

env = SmartEnv(**DEFAULTS)
