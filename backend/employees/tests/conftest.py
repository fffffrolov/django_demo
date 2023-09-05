from typing import Callable, Sequence

import pytest
from branches.tests.factories import BranchFactory
from employees.tests.factories import EmployeeFactory


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
def create_employee() -> Callable:
    def create(**kwargs) -> EmployeeFactory:
        return EmployeeFactory(**kwargs)
    return create
