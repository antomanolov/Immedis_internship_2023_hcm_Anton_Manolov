from rest_framework import serializers
from hcm_project.backend_api.appuser import AppUser

from hcm_project.backend_api.models.custom_user_model import Department

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        exclude = (
            'password', 'last_login', 'is_superuser','is_staff',
            'is_active','date_joined', 'groups', 'user_permissions'
            )