from django.contrib.gis.geos.point import Point
from django.utils.translation import gettext_lazy as _
from rest_framework.fields import Field


class LocationGISField(Field):
    default_error_messages = {
        'wrong_format': _('Wrong data format. Example: {"lng": 42.4351303, "lat": 19.2782777}'),
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.help_text = self.help_text or _('Format: {"lng": 42.4351303, "lat": 19.2782777}')

    def to_internal_value(self, data):
        if data.get('lng') is not None and data.get('lat') is not None:
            return Point(data['lng'], data['lat'], srid=4326)
        self.fail('wrong_format')

    def to_representation(self, value):
        try:
            return {'lng': value.x, 'lat': value.y}
        except IndexError:
            return None
