from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter

from app.admin import AppModelAdmin, AppTabularInline, admin
from employees.models import Employee


class EmployeeInline(AppTabularInline):
    model = Employee
    fields = ['_link', 'first_name', 'last_name', 'position']
    readonly_fields = ['_link']
    extra = 0

    def _link(self, obj):
        if obj.id is not None:
            return self.admin_edit_link(obj, f'{obj.id}: {obj.name}')
        return ''


@admin.register(Employee)
class EmployeeAdmin(AppModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'branch', 'position', 'created', 'modified']
    list_display_links = list_display
    list_filter = (
        ('branch', RelatedDropdownFilter),
        ('position', DropdownFilter),
    )

    search_fields = ['first_name', 'last_name']
    date_hierarchy = 'created'

    fieldsets = (
        (None, {
            'fields': (
                ('first_name', 'last_name'),
                'position',
                ('branch', 'branch_link'),
            ),
        }),
        (None, {
            'fields': (
                ('created', 'modified'),
            ),
        }),
    )
    autocomplete_fields = ['branch']
    readonly_fields = ('modified', 'created', 'branch_link')

    def get_queryset(self, request):
        return super().get_queryset(request).with_branch()

    def branch_link(self, obj):
        if obj.branch_id is not None:
            return self.admin_edit_link(obj.branch)
