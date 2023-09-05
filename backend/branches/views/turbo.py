from typing import Any

from app.views import BaseListView
from django.urls import reverse
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView

from branches.filters import BranchFilterSet
from branches.models import Branch


class BranchesListView(TemplateView):
    model = Branch
    template_name = 'branches/turbo/list.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update(
            frame='branches-list',
            frame_src=reverse('branches:turbo:frame-list'),
        )
        return context


class BranchDetailView(DetailView):
    model = Branch
    template_name = 'branches/turbo/detail.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        frame_src = reverse('employees:turbo:frame-list') + f'?branch={self.object.pk}'

        context.update(
            frame='employees-list',
            frame_src=frame_src,
        )
        return context


class BranchesListFrameView(BaseListView):
    model = Branch
    paginate_by = 5
    template_name = 'branches/turbo/_list.html'
    filterset_class = BranchFilterSet

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        url = reverse('branches:turbo:frame-list')
        if self.request.GET:
            url += f'?{self.request.GET.urlencode()}'

        context.update(
            url=url,
            frame='branches-list',
        )
        return context
