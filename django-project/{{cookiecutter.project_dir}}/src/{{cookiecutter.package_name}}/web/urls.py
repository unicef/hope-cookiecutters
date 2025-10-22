from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import HomeView, LoginView, HealthCheckView

app_name = "web"

urlpatterns = [
    path("", HomeView.as_view(), name="index"),
    path("healthcheck/", HealthCheckView.as_view(), name="login"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
