from django.core.management.base import BaseCommand

from branches.tests.factories import BranchFactory
from employees.tests.factories import EmployeeFactory


class Command(BaseCommand):
    """
    Fill db with faked data
    """
    def handle(self, *app_labels, **options):
        for b in range(10):
            branch = BranchFactory()
            for e in range(1000):
                EmployeeFactory(branch=branch)
