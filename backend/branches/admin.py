from app.admin import AppModelAdmin, admin
from branches.models import Branch
from django.utils.safestring import mark_safe
from employees.admin import EmployeeReadonlyTable
from rolepermissions.checkers import has_permission


@admin.register(Branch)
class BranchAdmin(AppModelAdmin):
    save_on_top = True
    list_display = ['id', 'name', 'admin_employees_count', 'created', 'modified']
    list_display_links = list_display
    search_fields = ['name']

    fieldsets = (
        (None, {
            'fields': (
                'name',
                'facade',
                'facade_preview',
                'location',
            ),
        }),
        (None, {
            'fields': (
                ('created', 'modified'),
                'admin_employees_count',
            ),
        }),
    )
    readonly_fields = ('modified', 'created', 'facade_preview', 'admin_employees_count')

    inlines = [EmployeeReadonlyTable]

    def get_readonly_fields(self, request, obj=None) -> tuple:
        readonly_fields = super().get_readonly_fields(request, obj)
        if not has_permission(request.user, 'edit_branch_map'):
            readonly_fields = tuple(readonly_fields) + ('location', )
        return readonly_fields

    def facade_preview(self, obj):
        if not obj.facade:
            return ''
        return mark_safe(f'<img src="{obj.facade.url}" width="auto" height="300" />')

    def get_queryset(self, request):
        return super().get_queryset(request).with_employees_count()

    def admin_employees_count(self, obj):
        return obj.employees_count
    admin_employees_count.admin_order_field = '_employees_count'    # type: ignore
    admin_employees_count.short_description = 'Total Employees'    # type: ignore
