from django_filters import rest_framework as filters

from branches.models import Branch


class BranchFilterSet(filters.FilterSet):
    search = filters.CharFilter(method='filter_by_search')
    o = filters.OrderingFilter(
        fields=(
            ('name', 'name'),
            ('created', 'created'),
            ('modified', 'modified'),
        ),
    )

    class Meta:
        model = Branch
        fields = ['search']

    def filter_by_search(self, queryset, name, value):
        return queryset.search(value)
