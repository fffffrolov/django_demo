import factory
from pytest_factoryboy import register

from branches.tests.factories import BranchFactory
from employees.models import Employee


@register
class EmployeeFactory(factory.django.DjangoModelFactory):
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    position = factory.Faker('job')
    branch = factory.SubFactory(BranchFactory)

    class Meta:
        model = Employee
