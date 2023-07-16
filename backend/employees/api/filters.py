from django_filters import rest_framework as filters

from employees.models import Employee


class EmployeeFilterSet(filters.FilterSet):
    search = filters.CharFilter(method='filter_by_search')
    branch_search = filters.CharFilter(method='filter_by_branch_search')
    o = filters.OrderingFilter(
        fields=(
            ('first_name', 'first_name'),
            ('last_name', 'last_name'),
            ('position', 'position'),
            ('branch__name', 'branch_name'),
            ('created', 'created'),
            ('modified', 'modified'),
        ),
    )

    class Meta:
        model = Employee
        fields = [
            'search',
            'branch',
        ]

    def filter_by_search(self, queryset, name, value):
        return queryset.search(value)

    def filter_by_branch_search(self, queryset, name, value):
        return queryset.branch_search(value)
