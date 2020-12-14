from behaviors.behaviors import Timestamped
from django.contrib.postgres.indexes import GinIndex

from app.models import AppModel, models


class EmployeeQuerySet(models.QuerySet):

    def search(self, query_string: str) -> models.QuerySet:
        # When searching for a person, the user usually expects the first or last name to start with their input.
        # We use ~~* (ILIKE) operator because we can increase this query productivity by GIN index.
        query = f'{str(query_string).strip()}%'
        return self.extra(where=['first_name ~~* %s OR last_name ~~* %s'], params=[query, query])

    def with_branch(self):
        return self.select_related('branch')


class Employee(Timestamped, AppModel):
    branch = models.ForeignKey(
        to='branches.Branch',
        related_name='employees',
        on_delete=models.SET_NULL,
        null=True, blank=True,
    )
    first_name = models.CharField(
        max_length=255,
        db_index=True,
    )
    last_name = models.CharField(
        max_length=255,
        db_index=True,
    )
    position = models.CharField(
        max_length=255,
        db_index=True,
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
