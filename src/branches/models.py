from __future__ import annotations

from typing import Sequence

from behaviors.behaviors import Timestamped
from django.contrib.gis.db.models import GeometryField
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import D
from django.contrib.postgres.indexes import GinIndex, GistIndex

from app.models import AppModel, models
from app.utils import RandomPath


class BranchQueryset(models.QuerySet):
    def search(self, query_string: str) -> models.QuerySet:
        query_string = str(query_string).strip()
        if len(query_string) < 3:
            query = f'{query_string}%'
        else:
            query = f'%{query_string}%'
        return self.extra(where=['name ILIKE %s'], params=[query])

    def with_employees_count(self) -> models.QuerySet:
        return self.annotate(_employees_count=models.Count('employees'))

    def annotate_not_far_away(self, coordinates: Sequence[float], radius :int = 30000) -> models.QuerySet:
        point = Point(*map(float, coordinates), srid=4326)

        return self.filter(
            geometry__dwithin=(point, D(m=radius)),
        ).annotate(
            distance=Distance('geometry', point),
        ).order_by('-distance')


class Branch(Timestamped, AppModel):
    location = GeometryField(
        geography=True,
        blank=True, null=True,
    )
    name = models.CharField(
        max_length=255,
        db_index=True,
    )
    facade = models.ImageField(
        blank=True,
        upload_to=RandomPath('branches/facades'),
    )

    objects = BranchQueryset.as_manager()

    class Meta:
        indexes = [
            GinIndex(name='branch_name_gin_trgm_index', fields=['name'], opclasses=['gin_trgm_ops']),
            GistIndex(fields=['location'], name='branch_location_gist_index'),
        ]

    @property
    def employees_count(self) -> int:
        if hasattr(self, '_employees_count'):
            self._employees_count : int
            return self._employees_count
        return self.employees.count()
