from rest_framework import serializers

from app.api.fields import LocationGISField
from branches.models import Branch


class BranchSerializer(serializers.ModelSerializer):
    location = LocationGISField()
    employees_count = serializers.SerializerMethodField()

    class Meta:
        model = Branch
        fields = [
            'id',
            'location',
            'name',
            'facade',
            'employees_count',
        ]
        read_only_fields = fields

    def get_employees_count(self, obj) -> int:
        """
        We could avoid duplicating functions. But type hinting makes API docs better.
        """
        return obj.employees_count  # type: ignore
