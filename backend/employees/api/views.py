from app.api.viewsets import ReadOnlyAppViewSet
from employees.filters import EmployeeFilterSet
from employees.models import Employee

from .pagination import EmployeePagination
from .serializers import EmployeeSerializer


class EmployeeViewSet(ReadOnlyAppViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.with_branch()
    filterset_class = EmployeeFilterSet
    pagination_class = EmployeePagination
