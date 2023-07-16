from rest_framework import serializers

from branches.api.serializers import BranchSmallSerializer
from employees.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    branch = BranchSmallSerializer(read_only=True)

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
