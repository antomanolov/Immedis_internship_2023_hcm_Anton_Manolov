from rest_framework import serializers
from hcm_project.backend_api.appuser import AppUser

from hcm_project.backend_api.models.custom_user_model import Department, JobTitle

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class JobTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobTitle
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        exclude = (
            'last_login', 'is_superuser','is_staff',
            'is_active','date_joined', 'groups', 'user_permissions'
            )
    
    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(user.password)
        user.save()
        return user

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    
    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        user = AppUser.objects.filter(email=email).first()
        
        if user and user.check_password(password):
            data['user'] = user
        else:
            raise serializers.ValidationError("Invalid email or password.")

        return data