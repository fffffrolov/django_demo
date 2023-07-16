import time
from typing import Any

from django.db import models
from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.conf import settings

from .models import Branch
from employees.models import Employee


class BranchDetailView(ListView):
    detail_context_object_name = 'object'
    model = Employee
    paginate_by = 100
    template_name = 'branches/detail.html'

    def get_queryset(self) -> models.query.QuerySet[Branch]:
        return super().get_queryset().filter(branch_id=self.kwargs.get('pk'))

    def get(self, request, *args, **kwargs):
        time.sleep(settings.DEFAULT_LOAD_DELAY)
        self.object = self.get_object()
        return super().get(request, *args, **kwargs)

    def get_queryset_for_object(self):
        return Branch.objects.all()

    def get_object(self):
        queryset = self.get_queryset_for_object()
        pk = self.kwargs.get('pk')
        if pk is None:
            raise AttributeError('pk expected in url')
        return get_object_or_404(queryset, pk=pk)

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        current_page = context['page_obj'].number
        context['counter_base'] = (current_page - 1) * self.paginate_by

        context[self.detail_context_object_name] = self.object
        return context


class BranchesListView(ListView):
    model = Branch
    paginate_by = 5
    template_name = 'branches/list.html'

    def get(self, request, *args, **kwargs):
        time.sleep(settings.DEFAULT_LOAD_DELAY)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        current_page = context['page_obj'].number
        context['counter_base'] = (current_page - 1) * self.paginate_by

        return context
