from rest_framework import generics
from hcm_project.backend_api.appuser import AppUser

from hcm_project.backend_api.models.custom_user_model import Department
from hcm_project.backend_api.serializers import DepartmentSerializer, EmployeeSerializer

class DepartmentList(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class EmployeeListByDep(generics.ListCreateAPIView):
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        department_name = self.kwargs['department']
        try:
            department = Department.objects.get(name=department_name)  
            return AppUser.objects.filter(department=department)
        except Department.DoesNotExist:
            # Handle the case where the department does not exist
            return AppUser.objects.none()