from typing import TypeVar

from factory.base import FactoryMetaClass
from factory.django import DjangoModelFactory

factories_registry = {}

T = TypeVar("T")


class AutoRegisterFactoryMetaClass(FactoryMetaClass):
    def __new__(cls, class_name, bases, attrs):
        new_class = super().__new__(cls, class_name, bases, attrs)
        factories_registry[new_class._meta.model] = new_class
        return new_class


class AutoRegisterModelFactory(DjangoModelFactory[T], metaclass=AutoRegisterFactoryMetaClass):
    def __call__(self, *args, **kwargs) -> T:
        return super().__call__(*args, **kwargs)


def get_factory_for_model(_model):
    class Meta:
        model = _model

    if _model in factories_registry:
        return factories_registry[_model]
    return type(f"{_model._meta.model_name}AutoFactory", (AutoRegisterModelFactory,), {"Meta": Meta})
