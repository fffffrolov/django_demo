import pytest

pytestmark = [pytest.mark.django_db]


def test_order_by_distance(api_client, get_point_inside_moscow, moscow_canter, outside_moscow, create_branches):
    moscow_branches = create_branches(3, location=get_point_inside_moscow)
    not_moscow_branches = create_branches(3, location=outside_moscow)

    response = api_client.get(
        f'/api/v1/branches/?location={moscow_canter[1]},{moscow_canter[0]}',
        format='json',
    ).json()
    filtered_branches_ids = [branch['id'] for branch in response['results']]

    assert len(filtered_branches_ids) == 3
    assert all([moscow_branch.id in filtered_branches_ids for moscow_branch in moscow_branches])
    assert all([not_moscow_branch.id not in filtered_branches_ids for not_moscow_branch in not_moscow_branches])


def test_n_plus_one_in_list(api_client, django_assert_max_num_queries, create_branches, create_employees):
    branches = create_branches(10)
    for branch in branches:
        create_employees(10, branch=branch)

    with django_assert_max_num_queries(2):
        api_client.get('/api/v1/branches/', format='json')


def test_search_branch(api_client, branch_with_keyword, branch_with_other_keyword, search_keyword):
    response = api_client.get(
        f'/api/v1/branches/?search={search_keyword}',
        format='json',
    ).json()
    filtered_branches_ids = [branch['id'] for branch in response['results']]

    assert branch_with_keyword.id in filtered_branches_ids
    assert branch_with_other_keyword.id not in filtered_branches_ids


def test_order_list_by_name_asc(api_client, create_branch):
    a_branch = create_branch(name='A branch')
    x_branch = create_branch(name='X branch')

    response = api_client.get(
        '/api/v1/branches/?o=name',
        format='json',
    ).json()
    filtered_branches_ids = [branch['id'] for branch in response['results']]

    assert filtered_branches_ids[0] == a_branch.id
    assert filtered_branches_ids[1] == x_branch.id


def test_order_list_by_name_desc(api_client, create_branch):
    a_branch = create_branch(name='A branch')
    x_branch = create_branch(name='X branch')

    response = api_client.get(
        '/api/v1/branches/?o=-name',
        format='json',
    ).json()
    filtered_branches_ids = [branch['id'] for branch in response['results']]

    assert filtered_branches_ids[0] == x_branch.id
    assert filtered_branches_ids[1] == a_branch.id
