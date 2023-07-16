from typing import Mapping, Optional

from django.contrib.gis.geos.point import Point
from django.utils.translation import gettext_lazy as _
from drf_yasg import openapi
from rest_framework.fields import Field

example_format = '{"lat": 42.4351303, "lng": 19.2782777}'


class LocationGISField(Field):
    default_error_messages = {
        'wrong_format': _(f'Wrong data format. Example: {example_format}'),
    }

    class Meta:
        swagger_schema_fields = {
            'type': openapi.TYPE_OBJECT,
            'title': 'Location',
            'properties': {
                'lat': openapi.Schema(
                    title='latitude',
                    format=openapi.FORMAT_FLOAT,
                    type=openapi.TYPE_NUMBER,
                ),
                'lng': openapi.Schema(
                    title='longitude',
                    format=openapi.FORMAT_FLOAT,
                    type=openapi.TYPE_NUMBER,
                ),
            },
            'required': ['lat', 'lng'],
        }

    def __init__(self, *args, **kwargs):
        kwargs.setdefault(
            'help_text', _(f'Format: {example_format}'),
        )
        super().__init__(*args, **kwargs)

    def to_internal_value(self, data: dict) -> Point:
        if data.get('lng') is not None and data.get('lat') is not None:
            return Point(data['lng'], data['lat'], srid=4326)
        self.fail('wrong_format')

    def to_representation(self, value: Point) -> Optional[Mapping[str, float]]:
        try:
            return {'lat': value.y, 'lng': value.x}
        except IndexError:
            return None
