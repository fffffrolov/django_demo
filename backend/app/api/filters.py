from django_filters import rest_framework as filters


class NumberInFilter(filters.BaseCSVFilter, filters.NumberFilter):
    pass
