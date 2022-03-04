from typing import Iterable, Type

from automapper import Mapper
from django.db import models


def spec_function(target_cls: Type[models.Model]) -> Iterable[str]:
    return (field_name.attname for field_name in target_cls._meta.concrete_fields)


def extend(mapper: Mapper) -> None:
    mapper.add_spec(models.Model, spec_function)
