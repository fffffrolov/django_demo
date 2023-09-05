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

    def add_arguments(self, parser):
        parser.add_argument('total_branches', type=int, default=10)
        parser.add_argument('employees_per_branch', type=int, default=200)
        parser.add_argument('total_jobs', type=int, default=10)

    def handle(self, *app_labels, **options):
        total_branches = options['total_branches']
        employees_per_branch = options['employees_per_branch']

        progress = tqdm.tqdm(total=total_branches * employees_per_branch)

        fake = Faker()
        jobs = [fake.unique.job() for _ in range(options['total_jobs'])]

        for _ in range(total_branches):
            branch = BranchFactory()
            for _ in range(employees_per_branch):
                EmployeeFactory(branch=branch, position=random.choice(jobs))
                progress.update()
