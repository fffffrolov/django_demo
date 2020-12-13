from rest_framework import serializers

from branches.api.serializers import BranchSerializer
from employees.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    branch = BranchSerializer(read_only=True)

    class Meta:
        model = Employee
        fields = [
            'id',
            'branch',
            'first_name',
            'last_name',
            'position',
        ]
        read_only_fields = fields
