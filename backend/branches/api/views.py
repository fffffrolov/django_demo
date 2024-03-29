from app.api.viewsets import ReadOnlyAppViewSet
from branches.api.serializers import BranchSerializer
from branches.filters import BranchFilterSet
from branches.models import Branch


class BranchViewSet(ReadOnlyAppViewSet):
    serializer_class = BranchSerializer
    queryset = Branch.objects.with_employees_count()
    filterset_class = BranchFilterSet
