from decimal import Decimal
from typing import Sequence, Union

from django.db import models
from django_filters import rest_framework as filters

from app.api.filters import NumberInFilter
from branches.models import Branch, BranchQueryset


class BranchFilterSet(filters.FilterSet):
    search = filters.CharFilter(method='filter_by_search')
    location = NumberInFilter(method='filter_by_location')
    o = filters.OrderingFilter(
        fields=(
            ('name', 'name'),
            ('created', 'created'),
            ('modified', 'modified'),
        ),
    )

    class Meta:
        model = Branch
        fields = ['search']

    def filter_by_search(self,
                         queryset: BranchQueryset,
                         name: str,
                         value: str) -> models.QuerySet:
        return queryset.search(value)

    def filter_by_location(self,
                           queryset: BranchQueryset,
                           name: str,
                           value: Sequence[Union[Decimal, int]]) -> models.QuerySet:
        if len(value) > 3 or len(value) < 2:
            return queryset.none()
        return queryset.order_by_distance(*value)
