from django.conf import settings
from django.urls import include
from django.contrib.admin import site
from django.urls import path
from django.views.static import serve
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

handler400 = "{{cookiecutter.package_name}}.web.views.handler400"
handler403 = "{{cookiecutter.package_name}}.web.views.handler403"
handler404 = "{{cookiecutter.package_name}}.web.views.handler404"
handler500 = "{{cookiecutter.package_name}}.web.views.handler500"

urlpatterns = [
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/schema/swagger-ui/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("api/schema/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    path("api/", include("{{cookiecutter.package_name}}.api.urls"), name="api"),
    path("favicon.ico", serve, kwargs={"document_root": settings.STATIC_ROOT, "path": "favicon.ico"}),
    path("admin/", site.urls),
    path("social/", include("social_django.urls", namespace="social")),
    path("issues/", include("issues.urls")),
    path("adminactions/", include("adminactions.urls")),
    path("", include("{{cookiecutter.package_name}}.web.urls")),
]

if settings.DEBUG:
    if "debug_toolbar.middleware.DebugToolbarMiddleware" in settings.MIDDLEWARE:
        import debug_toolbar

        urlpatterns = [
            path(r"__debug__/", include(debug_toolbar.urls)),
        ] + urlpatterns

    if "django_browser_reload.middleware.BrowserReloadMiddleware" in settings.MIDDLEWARE:
        urlpatterns += [
            path("__reload__/", include("django_browser_reload.urls")),
        ]

urlpatterns = [path(settings.URL_PREFIX, include(urlpatterns))]  # type: ignore[arg-type]
