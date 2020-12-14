import random
from typing import Callable, Sequence

import pytest
from django.contrib.gis.geos.point import Point
from pytest_factoryboy import register

from branches.tests.factories import BranchFactory
from employees.tests.factories import EmployeeFactory

register(BranchFactory)


@pytest.fixture
def search_keyword() -> str:
    return 'Slytherin'


@pytest.fixture
def other_search_keyword() -> str:
    return 'Gryffindor'


@pytest.fixture
def moscow_canter() -> Point:
    return Point(37.617635, 55.755814, srid=4326)


@pytest.fixture
def outside_moscow() -> Point:
    return Point(82.920430, 55.030199, srid=4326)


@pytest.fixture
def get_point_inside_moscow() -> Callable:
    def get_point() -> Point:
        return Point(random.uniform(37.583104, 37.656568), random.uniform(55.773044, 55.755814), srid=4326)
    return get_point


@pytest.fixture
def create_branches() -> Callable:
    def create(total=1, **kwargs) -> Sequence[BranchFactory]:
        return [BranchFactory(**kwargs) for _ in range(total)]
    return create


@pytest.fixture
def create_employees() -> Callable:
    def create(total=1, **kwargs) -> Sequence[EmployeeFactory]:
        return [EmployeeFactory(**kwargs) for _ in range(total)]
    return create


@pytest.fixture
def branch_with_keyword(search_keyword: str) -> BranchFactory:
    return BranchFactory(name=f'Name with keyword {search_keyword}')


@pytest.fixture
def branch_with_other_keyword(other_search_keyword: str) -> BranchFactory:
    return BranchFactory(name=f'Name with keyword {other_search_keyword}')
