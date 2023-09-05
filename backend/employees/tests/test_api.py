import pytest

pytestmark = [pytest.mark.django_db]


@pytest.fixture
def adam(create_employee):
    return create_employee(first_name='Adam', last_name='Adamson', branch__name='A Branch', position='architect')


@pytest.fixture
def bernie(create_employee):
    return create_employee(first_name='Bernie', last_name='Bernieson', branch__name='X Branch', position='lumberjack')


def test_n_plus_one_in_list(api_client, django_assert_max_num_queries, create_branches, create_employees):
    branches = create_branches(10)
    for branch in branches:
        create_employees(10, branch=branch)

    with django_assert_max_num_queries(2):
        api_client.get('/api/v1/employees/', format='json')


def test_search_by_name(api_client, create_employee):
    employee = create_employee()
    response = api_client.get(
        f'/api/v1/employees/?search={employee.first_name[:-3]}',
        format='json',
    ).json()
    filtered_ids = [employee['id'] for employee in response['results']]

    assert employee.id in filtered_ids


def test_search_by_branch_name(api_client, create_employee):
    employee = create_employee()

    response = api_client.get(
        f'/api/v1/employees/?search={employee.branch.name}',
        format='json',
    ).json()
    filtered_ids = [employee['id'] for employee in response['results']]

    assert employee.id in filtered_ids


def test_filter_by_branch(api_client, create_employee):
    employee = create_employee()

    response = api_client.get(
        f'/api/v1/employees/?branch={employee.branch_id}',
        format='json',
    ).json()
    filtered_ids = [employee['id'] for employee in response['results']]

    assert employee.id in filtered_ids


@pytest.mark.parametrize(
    ('order_field', 'adam_index', 'bernie_index'),
    [
        ('first_name', 0, 1),
        ('-first_name', 1, 0),
        ('last_name', 0, 1),
        ('-branch_name', 1, 0),
        ('branch_name', 0, 1),
        ('-branch_name', 1, 0),
        ('position', 0, 1),
        ('-position', 1, 0),
    ],
)
def test_order_list_by(api_client, adam, bernie, order_field, adam_index, bernie_index):
    response = api_client.get(
        f'/api/v1/employees/?o={order_field}',
        format='json',
    ).json()
    filtered_ids = [employee['id'] for employee in response['results']]

    assert filtered_ids[adam_index] == adam.id
    assert filtered_ids[bernie_index] == bernie.id
