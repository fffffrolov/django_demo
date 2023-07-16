import time
from typing import Any

from django.conf import settings
from django.db import models
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Employee


class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'employees/detail.html'

    def get_queryset(self) -> models.query.QuerySet[Employee]:
        return super().get_queryset().with_branch()

    def get(self, request, *args, **kwargs):
        time.sleep(settings.DEFAULT_LOAD_DELAY)
        return super().get(request, *args, **kwargs)


class EmployeeListView(ListView):
    model = Employee
    paginate_by = 100
    template_name = 'employees/list.html'

    def get_queryset(self) -> models.query.QuerySet[Employee]:
        return super().get_queryset().with_branch()

    def get(self, request, *args, **kwargs):
        time.sleep(settings.DEFAULT_LOAD_DELAY)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        current_page = context['page_obj'].number
        context['counter_base'] = (current_page - 1) * self.paginate_by

        return context
