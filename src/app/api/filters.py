from django.contrib.gis.geos import GEOSGeometry
from django.contrib.gis.measure import D
from django_filters import rest_framework as filters


class MultiValueCoordsFilter(filters.BaseCSVFilter, filters.NumberFilter):

    def __init__(self, default_radius=10000, *args, **kwargs):
        self.default_radius = default_radius
        super().__init__(*args, **kwargs)

    def filter(self, qs, value):
        values = value or []
        allow_filter = len(values) >= 2
        latitude, longitude, radius = .0, .0, self.default_radius

        if len(values) == 2:
            latitude, longitude = values
        if len(values) == 3:
            latitude, longitude, radius = values

        if allow_filter:
            point = 'POINT({lat} {lng})'.format(lat=latitude, lng=longitude)
            pnt = GEOSGeometry(geo_input=point, srid=4326)
            qs = self.get_method(qs)(**{f'{self.field_name}__dwithin': (pnt, D(m=radius))})
        return qs
