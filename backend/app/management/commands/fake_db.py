import random

import tqdm
from branches.tests.factories import BranchFactory
from django.core.management.base import BaseCommand
from employees.tests.factories import EmployeeFactory
from faker import Faker


class Command(BaseCommand):
    """
    Fill db with faked data
    """

    def handle(self, *app_labels, **options):
        total_branches = 10
        branch_employee = 200
        total_jobs = 10
        progress = tqdm.tqdm(total=total_branches * branch_employee)

        fake = Faker()
        jobs = [fake.unique.job() for _ in range(total_jobs)]

        for _ in range(total_branches):
            branch = BranchFactory()
            for _ in range(branch_employee):
                EmployeeFactory(branch=branch, position=random.choice(jobs))
                progress.update()
