from __future__ import annotations

from copy import copy
from itertools import chain
from typing import Any, Optional, Sequence

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import FieldDoesNotExist
from django.db import models


class AppModel(models.Model):
    """
    Base class for models with common shortcuts
    """
    class Meta:
        abstract = True

    def __str__(self):
        """
        Default name for all models
        """
        if hasattr(self, 'name'):
            return str(self.name)
        return super().__str__()

    @classmethod
    def get_contenttype(cls) -> ContentType:
        return ContentType.objects.get_for_model(cls)

    @classmethod
    def has_field(cls, field: str) -> bool:
        """
        Shortcut to check if the model has a particular field
        """
        try:
            cls._meta.get_field(field)
            return True
        except FieldDoesNotExist:
            return False

    @classmethod
    def get_label(cls) -> str:
        """
        Get a unique within the app model label
        """
        return cls._meta.label_lower.split('.')[-1]

    def copy(self, **kwargs) -> AppModel:
        """
        Creates new instance from current
        """
        instance = copy(self)
        kwargs.update({
            'id': None,
            'pk': None,
        })
        instance.update_from_kwargs(**kwargs)
        return instance

    def update_from_kwargs(self, **kwargs):
        """
        A shortcut method to update an instance from the kwargs
        """
        for (key, value) in kwargs.items():
            setattr(self, key, value)

    def setattr_and_save(self, key: str, value: Any):
        """
        Shortcut for testing -- set attribute of the model and save
        """
        setattr(self, key, value)
        self.save(update_fields=[key])

    def to_dict(self,
                fields: Optional[Sequence[str]] = None,
                exclude: Optional[Sequence[str]] = None) -> dict:
        """
        return dict from instance data
        """
        data = {}
        _data = self.__dict__
        for field in chain(self._meta.concrete_fields, self._meta.private_fields):
            if isinstance(field, GenericForeignKey):
                continue
            if fields is not None and field.name not in fields:
                continue
            if exclude is not None and field.name in exclude:
                continue
            if field.name not in _data.keys() and f'{field.name}_id' not in _data.keys():
                continue

            key = field.name
            if isinstance(field, models.ForeignKey) or isinstance(field, models.OneToOneField):
                key = f'{field.name}_id'

            data[key] = field.value_from_object(self)
        return data
