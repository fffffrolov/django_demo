from django_filters import rest_framework as filters


class MultiValueCoordsFilter(filters.BaseCSVFilter, filters.NumberFilter):

    def __init__(self, default_radius: int = 10000, *args, **kwargs):
        self.default_radius = default_radius
        super().__init__(*args, **kwargs)

    def filter(self, qs, value):
        values = value or []
        latitude, longitude, radius = .0, .0, self.default_radius

        if len(values) == 2:
            latitude, longitude = values
        if len(values) == 3:
            latitude, longitude, radius = values

        return super().filter(qs, (latitude, longitude, radius))
