from typing import Any

from app.views import BaseListView
from django.db import models
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, reverse

from employees.models import Employee
from employees.filters import EmployeeFilterSet


class EmployeesListView(BaseListView):
    model = Employee
    paginate_by = 100
    template_name = 'employees/classic/list.html'
    filterset_class = EmployeeFilterSet

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        url = reverse('employees:classic:list')

        context.update(url=url)
        return context


class EmployeeDetailView(BaseListView):
    model = Employee
    detail_context_object_name = 'object'
    paginate_by = 100
    template_name = 'employees/classic/detail.html'

    def get_queryset(self) -> models.query.QuerySet[Employee]:
        queryset = super().get_queryset()
        return (
            queryset
            .filter(branch_id=self.object.branch_id, position=self.object.position)
            .exclude(pk=self.object.pk)
        )

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        self.object = self.get_object()
        return super().get(request, *args, **kwargs)

    def get_queryset_for_object(self) -> models.query.QuerySet[Employee]:
        return Employee.objects.all()

    def get_object(self) -> Employee:
        queryset = self.get_queryset_for_object()

        pk = self.kwargs.get('pk')
        if pk is None:
            raise AttributeError('pk expected in url')

        return get_object_or_404(queryset, pk=pk)

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        context[self.detail_context_object_name] = self.object

        url = reverse('employees:classic:detail', kwargs={'pk': self.object.pk})
        context.update(url=url)

        return context
