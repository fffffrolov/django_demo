from behaviors.behaviors import Timestamped
from django.contrib.postgres.indexes import GinIndex

from app.models import AppModel, models


class EmployeeQuerySet(models.QuerySet):

    def search(self, query_string: str) -> models.QuerySet:
        query_string = str(query_string).strip()
        if len(query_string) < 3:
            query = f'{query_string}%'
        else:
            query = f'%{query_string}%'
        return self.extra(where=['first_name ILIKE %s OR last_name ILIKE %s'], params=[query, query])


class Employee(Timestamped, AppModel):
    branch = models.ForeignKey(
        to='branches.Branch',
        related_name='employees',
        on_delete=models.SET_NULL,
        null=True, blank=True,
    )
    first_name = models.CharField(
        max_length=255,
    )
    last_name = models.CharField(
        max_length=255,
    )
    position = models.CharField(
        max_length=255,
    )

    objects = EmployeeQuerySet.as_manager()

    class Meta:
        indexes = [
            GinIndex(name='employee_fname_gin_index', fields=['first_name'], opclasses=['gin_trgm_ops']),
            GinIndex(name='employee_lname_gin_index', fields=['last_name'], opclasses=['gin_trgm_ops']),
        ]

    @property
    def name(self) -> str:
        return ' '.join([name for name in [self.first_name, self.last_name] if name])
