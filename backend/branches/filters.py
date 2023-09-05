from decimal import Decimal
from typing import Sequence, Union

from app.api.filters import NumberInFilter
from branches.models import Branch, BranchQueryset
from django.contrib.gis.db.models import GeometryField
from django.db import models
from django_filters import rest_framework as filters


class BranchFilterSet(filters.FilterSet):
    search = filters.CharFilter(method='filter_by_search')
    geo = NumberInFilter(method='filter_by_location')
    o = filters.OrderingFilter(
        fields=(
            ('name', 'name'),
            ('created', 'created'),
            ('modified', 'modified'),
        ),
    )

    class Meta:
        model = Branch
        fields = ['search', 'geo']
        exclude = ['location']

    def filter_by_search(
        self, queryset: BranchQueryset, _: str, value: str,
    ) -> models.QuerySet:
        return queryset.search(value)

    def filter_by_location(
        self, queryset: BranchQueryset, _: str, value: Sequence[Union[Decimal, int]],
    ) -> models.QuerySet:
        if len(value) > 3 or len(value) < 2:
            return queryset.none()
        return queryset.order_by_distance(*value)
