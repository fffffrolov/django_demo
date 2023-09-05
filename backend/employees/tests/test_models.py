import pytest
from employees.models import Employee
from employees.tests.factories import EmployeeFactory

pytestmark = [pytest.mark.django_db]


@pytest.fixture
def employee_with_name(request, create_employee) -> EmployeeFactory:
    return create_employee(first_name=request.param[0], last_name=request.param[1])


@pytest.mark.parametrize(
    ('employee_with_name', 'search', 'in_search'),
    [
        (('Adam', 'Adamson'), 'ada', True),
        (('Adam', 'Adamson'), 'ber', False),
        (('Bernie', 'Bernieson'), 'ada', False),
        (('Bernie', 'Bernieson'), 'ber', True),
    ],
    indirect=['employee_with_name'],
)
def test_search_by_first_letters(employee_with_name, search, in_search):
    filtered = Employee.objects.search(search).values_list('id', flat=True)

    assert (employee_with_name.id in filtered) is in_search


@pytest.mark.parametrize(
    ('employee_with_name', 'search', 'in_search'),
    [
        (('Adam', 'Adamson'), 'Adam', True),
        (('Adam', 'Adamson'), 'Bernie', False),
        (('Bernie', 'Bernieson'), 'Adam', False),
        (('Bernie', 'Bernieson'), 'Bernie', True),
    ],
    indirect=['employee_with_name'],
)
def test_search_by_name(employee_with_name, search, in_search):
    filtered = Employee.objects.search(search).values_list('id', flat=True)

    assert (employee_with_name.id in filtered) is in_search


@pytest.mark.parametrize(
    ('employee_with_name', 'search', 'in_search'),
    [
        (('Adam', 'Adamson'), 'Adamson', True),
        (('Adam', 'Adamson'), 'Bernieson', False),
        (('Bernie', 'Bernieson'), 'Adamson', False),
        (('Bernie', 'Bernieson'), 'Bernieson', True),
    ],
    indirect=['employee_with_name'],
)
def test_search_by_surname(employee_with_name, search, in_search):
    filtered = Employee.objects.search(search).values_list('id', flat=True)

    assert (employee_with_name.id in filtered) is in_search


@pytest.mark.parametrize(
    ('employee_with_name', 'search', 'in_search'),
    [
        (('Adam', 'Adamson'), 'dam', False),
        (('Adam', 'Adamson'), 'erni', False),
        (('Bernie', 'Bernieson'), 'dam', False),
        (('Bernie', 'Bernieson'), 'erni', False),
    ],
    indirect=['employee_with_name'],
)
def test_search_without_first_letters(employee_with_name, search, in_search):
    filtered = Employee.objects.search(search).values_list('id', flat=True)

    assert (employee_with_name.id in filtered) is in_search


def test_search_by_branch_name(create_employee):
    employee = create_employee()

    filtered = Employee.objects.search(employee.branch.name).values_list('id', flat=True)

    assert employee.id in filtered


def test_search_by_branch_name_part(create_employee):
    employee = create_employee(branch__name='Branch with several worlds in name')

    first_word = employee.branch.name.split(' ')[0]
    filtered = Employee.objects.search(first_word).values_list('id', flat=True)

    assert employee.id in filtered
