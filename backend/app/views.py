from typing import Any

from django_filters.views import FilterView


class BaseListView(FilterView):
    paginate_by = 100

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        current_page = context['page_obj'].number
        context['counter_base'] = (current_page - 1) * self.paginate_by

        return context
