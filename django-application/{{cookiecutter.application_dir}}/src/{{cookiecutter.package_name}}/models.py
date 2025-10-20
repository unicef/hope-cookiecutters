from django.db import models


class AppModel(models.Model):
    def __str__(self) -> str:
        return self.__class__.__name__
