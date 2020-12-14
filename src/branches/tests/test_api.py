import json

import pytest

pytestmark = [pytest.mark.django_db]


def test_order_by_distance(api_client, get_point_inside_moscow, moscow_canter, outside_moscow, create_branches):
    moscow_branches = create_branches(3, location=get_point_inside_moscow)
    not_moscow_branches = create_branches(3, location=outside_moscow)

    response = api_client.get(
        f'/api/v1/branches/?location={moscow_canter[1]},{moscow_canter[0]}',
        format='json',
    )
    filtered_branches = json.loads(response.content.decode('utf-8', errors='ignore'))
    filtered_branches_ids = [branch['id'] for branch in filtered_branches['results']]

    assert len(filtered_branches_ids) == 3
    assert all([moscow_branch.id in filtered_branches_ids for moscow_branch in moscow_branches])
    assert all([not_moscow_branch.id not in filtered_branches_ids for not_moscow_branch in not_moscow_branches])
