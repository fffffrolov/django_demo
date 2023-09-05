from typing import Any

from app.views import BaseListView
from django.db import models
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, reverse
from employees.models import Employee
from employees.filters import EmployeeFilterSet

from branches.models import Branch
from branches.filters import BranchFilterSet


class BranchesListView(BaseListView):
    model = Branch
    paginate_by = 5
    template_name = 'branches/classic/list.html'
    filterset_class = BranchFilterSet

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        url = reverse('branches:classic:list')

        context.update(url=url)
        return context


class BranchDetailView(BaseListView):
    model = Employee
    detail_context_object_name = 'object'
    paginate_by = 100
    template_name = 'branches/classic/detail.html'
    filterset_class = EmployeeFilterSet

    def get_queryset(self) -> models.query.QuerySet[Branch]:
        return super().get_queryset().filter(branch_id=self.kwargs.get('pk'))

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        self.object = self.get_object()
        return super().get(request, *args, **kwargs)

    def get_queryset_for_object(self) -> models.query.QuerySet[Branch]:
        return Branch.objects.all()

    def get_object(self) -> Branch:
        queryset = self.get_queryset_for_object()

        pk = self.kwargs.get('pk')
        if pk is None:
            raise AttributeError('pk expected in url')

        return get_object_or_404(queryset, pk=pk)

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        context[self.detail_context_object_name] = self.object

        url = reverse('branches:classic:detail', kwargs={'pk': self.object.pk})
        context.update(url=url)

        return context
