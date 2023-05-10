from functools import partial
from typing import Any, Dict, Type

import factory
from factory.base import StubObject
from factory.django import DjangoModelFactory

from django.forms.models import model_to_dict


def generate_dict_build_factory(factory: DjangoModelFactory):
    """
        Generate a function that when it is called generate a dict of factory model
    Args:
        factory: Model Factory

    Returns:
        partial
    """

    def convert_dict_from_stub(stub: StubObject) -> Dict[str, Any]:
        stub_dict = stub.__dict__
        for key, value in stub_dict.items():
            if isinstance(value, StubObject):
                stub_dict[key] = convert_dict_from_stub(value)
        return stub_dict

    def dict_factory(factory, **kwargs):
        stub = factory.stub(**kwargs)
        stub_dict = convert_dict_from_stub(stub)
        return stub_dict

    return partial(dict_factory, factory)


def generate_dict_factory(factory: Type[DjangoModelFactory]):
    """
        Generate a function that when it is called generate a dict of factory model
    Args:
        build: boolean
        factory: Model Factory

    Returns:
        partial
    """

    def serial_model(modelobj):
        opts = modelobj._meta.fields
        modeldict = model_to_dict(modelobj)
        for m in opts:
            if m.is_relation:
                foreignkey = getattr(modelobj, m.name)
                if foreignkey:
                    try:
                        modeldict[m.name] = serial_model(foreignkey)
                    except:
                        pass
        return modeldict

    def dict_factory(factory, build=False, **kwargs):
        if build:
            instance = factory.build(**kwargs)
        else:
            instance = factory(**kwargs)
        instance_dict = serial_model(instance)
        return instance_dict

    return partial(dict_factory, factory)


def build_dict(factory_class: Type[DjangoModelFactory], **kwargs):
    return factory.build(
        dict, FACTORY_CLASS=factory_class, **kwargs
    )
