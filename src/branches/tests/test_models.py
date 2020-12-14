import pytest

from branches.models import Branch

pytestmark = [pytest.mark.django_db]


def test_order_by_distance(get_point_inside_moscow, moscow_canter, outside_moscow, create_branches):
    moscow_branches = create_branches(3, location=get_point_inside_moscow)
    not_moscow_branches = create_branches(3, location=outside_moscow)

    filtered_branches_ids = Branch.objects.order_by_distance(
        moscow_canter[1], moscow_canter[0],
    ).values_list('id', flat=True)

    assert len(filtered_branches_ids) == 3
    assert all([moscow_branch.id in filtered_branches_ids for moscow_branch in moscow_branches])
    assert all([not_moscow_branch.id not in filtered_branches_ids for not_moscow_branch in not_moscow_branches])


def test_n_plus_one_in_list(django_assert_max_num_queries, create_branches, create_employees):
    branches = create_branches(3)
    for branch in branches:
        create_employees(10, branch=branch)

    with django_assert_max_num_queries(1):
        branches = Branch.objects.with_employees_count()
        for branch in branches:
            _ = branch.employees_count


def test_search_by_keyword(branch_with_keyword, branch_with_other_keyword, search_keyword, other_search_keyword):
    keyword_search = Branch.objects.search(search_keyword).values_list('id', flat=True)
    other_keyword_search = Branch.objects.search(other_search_keyword).values_list('id', flat=True)

    assert branch_with_keyword.id in keyword_search
    assert branch_with_other_keyword.id not in keyword_search
    assert branch_with_keyword.id not in other_keyword_search


def test_search_by_part_of_name(branch_with_keyword, branch_with_other_keyword):
    search_query = 'Name with keyword'
    search = Branch.objects.search(search_query).values_list('id', flat=True)

    assert len(search) == 2
    assert branch_with_keyword.id in search
    assert branch_with_other_keyword.id in search


def test_search_by_whole_name(branch_with_keyword):
    assert branch_with_keyword.id in Branch.objects.search(branch_with_keyword.name).values_list('id', flat=True)
