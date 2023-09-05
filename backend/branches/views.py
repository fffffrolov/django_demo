from typing import Any

from app.views import BaseListView
from django.db import models
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from employees.filters import EmployeeFilterSet
from employees.models import Employee

from .filters import BranchFilterSet
from .models import Branch


class BranchesListView(TemplateView):
    model = Branch
    template_name = 'branches/list.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update(
            frame='branches-list',
            frame_src=reverse('branches:frame-list'),
        )
        return context


class BranchDetailView(DetailView):
    model = Branch
    template_name = 'branches/detail.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        frame_src = reverse('employees:frame-list') + f'?branch={self.object.pk}'

        context.update(
            frame='employees-list',
            frame_src=frame_src,
        )
        return context


class BranchClassicDetailView(BaseListView):
    model = Employee
    detail_context_object_name = 'object'
    paginate_by = 10
    template_name = 'branches/detail.html'
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

        return context


class BranchesListFrameView(BaseListView):
    model = Branch
    paginate_by = 5
    template_name = 'branches/_list.html'
    filterset_class = BranchFilterSet

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        url = reverse('branches:frame-list')
        if self.request.GET:
            url += f'?{self.request.GET.urlencode()}'

        context.update(
            url=url,
            frame='branches-list',
        )
        return context
