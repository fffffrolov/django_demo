from app.api.viewsets import ReadOnlyAppViewSet
from employees.api.filters import EmployeeFilterSet
from employees.api.serializers import EmployeeSerializer
from employees.models import Employee


class EmployeeViewSet(ReadOnlyAppViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.with_branch()
    filterset_class = EmployeeFilterSet
