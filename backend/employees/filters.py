from django_filters import rest_framework as filters
from employees.models import Employee


class EmployeeFilterSet(filters.FilterSet):
    search = filters.CharFilter(method='filter_by_search')
    exclude = filters.NumberFilter(method='filter_by_exclude')
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
        fields = ['search', 'branch', 'position']

    def filter_by_search(self, queryset, _, value):
        return queryset.search(value)

    def filter_by_exclude(self, queryset, _, value):
        return queryset.exclude(id=value)
