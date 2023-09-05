from typing import Any

from app.views import BaseListView
from django.db import models
from django.urls import reverse
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView

from employees.filters import EmployeeFilterSet
from employees.models import Employee


class EmployeesListView(TemplateView):
    model = Employee
    template_name = 'employees/turbo/list.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update(
            frame='employees-list',
            frame_src=reverse('employees:turbo:frame-list'),
        )
        return context


class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'employees/turbo/detail.html'

    def get_queryset(self) -> models.query.QuerySet[Employee]:
        return super().get_queryset().with_branch()

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        frame_src = (
            reverse('employees:turbo:frame-list')
            + f'?branch={self.object.branch_id}'
            + f'&exclude={self.object.id}'
            + f'&position={self.object.position}'
        )
        context.update(
            frame='employees-list',
            frame_src=frame_src
        )
        return context


class EmployeeListFrameView(BaseListView):
    model = Employee
    paginate_by = 100
    template_name = 'employees/turbo/_list.html'
    filterset_class = EmployeeFilterSet

    def get_queryset(self) -> models.query.QuerySet[Employee]:
        return super().get_queryset().with_branch()

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        url = reverse('employees:turbo:frame-list')
        if self.request.GET:
            url += f'?{self.request.GET.urlencode()}'

        context.update(
            url=url,
            frame='employees-list',
        )
        return context
