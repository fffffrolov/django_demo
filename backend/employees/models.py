from app.models import AppModel, WordSimilarityQuerySet
from behaviors.behaviors import Timestamped
from django.contrib.postgres.indexes import GinIndex
from django.db import models


class EmployeeQuerySet(WordSimilarityQuerySet):

    def search(self, query_string: str) -> models.QuerySet:
        # When searching for a person, the user usually expects the first or last name to start with their input.

        query_string = query_string.strip()

        return self.annotate(
            branch_name=models.F('branch__name'),
        ).with_word_similarity(
            'branch_name', query_string,
        ).filter(
            models.Q(word_similarity__gte=0.5)
            | models.Q(first_name__istartswith=query_string)
            | models.Q(last_name__istartswith=query_string)
        ).order_by('-word_similarity')

    def with_branch(self) -> models.QuerySet:
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
        ordering = ['-branch', 'position', 'last_name']
        indexes = [
            GinIndex(name='employee_fname_gin_index', fields=['first_name'], opclasses=['gin_trgm_ops']),
            GinIndex(name='employee_lname_gin_index', fields=['last_name'], opclasses=['gin_trgm_ops']),
        ]

    @property
    def name(self) -> str:
        return ' '.join([name for name in [self.first_name, self.last_name] if name])
