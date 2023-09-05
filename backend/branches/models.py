from __future__ import annotations

from decimal import Decimal

from app.models import AppModel, WordSimilarityQuerySet, models
from app.utils import RandomPath
from behaviors.behaviors import Timestamped
from django.contrib.gis.db.models import GeometryField
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos.point import Point
from django.contrib.gis.measure import D
from django.contrib.postgres.indexes import GistIndex


class BranchQueryset(WordSimilarityQuerySet):

    def search(self, query_string: str) -> models.QuerySet:
        # Branch name can consist of several words.
        # When searching, the user may forget some of the words or their order.
        # Therefore, we show him those entries that contain at least half of the words he specified.
        return self.with_word_similarity(
            'name', query_string,
        ).filter(
            word_similarity__gte=0.5,
        ).order_by('-word_similarity')

    def with_employees_count(self) -> models.QuerySet:
        return self.annotate(_employees_count=models.Count('employees'))

    def order_by_distance(self,
                          latitude: Decimal,
                          longitude: Decimal,
                          max_radius: int = 30000) -> models.QuerySet:
        point = Point(float(longitude), float(latitude), srid=4326)

        return self.filter(
            # Distance is an expensive operation.
            # This is why we exclude objects that are too far away from the search point.
            location__dwithin=(point, D(m=int(max_radius))),
        ).annotate(
            distance=Distance('location', point),
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
        ordering = ['-id']
        indexes = [
            GistIndex(name='branch_name_gist_trgm_index', fields=['name'], opclasses=['gist_trgm_ops']),
        ]

    @property
    def employees_count(self) -> int:
        if hasattr(self, '_employees_count'):
            return self._employees_count    # type: ignore
        return self.employees.count()
