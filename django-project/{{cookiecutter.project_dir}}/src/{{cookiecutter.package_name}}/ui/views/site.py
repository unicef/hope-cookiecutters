from django.views.generic import TemplateView
from django.views import View
from django.http import HttpRequest, HttpResponse
from ._common import MediaMixin


class HomeView(TemplateView):
    template_name = "pages/index.html"


class HealthCheckView(MediaMixin, View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return HttpResponse("Ok")
