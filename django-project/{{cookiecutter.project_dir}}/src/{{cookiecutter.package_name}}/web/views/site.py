from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView as DjangoLoginView
from django.views import View
from django.http import HttpRequest, HttpResponse


class HomeView(TemplateView):
    template_name = "home.html"


class HealthCheckView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return HttpResponse("Ok")


class LoginView(DjangoLoginView):
    pass
