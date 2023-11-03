from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from hcm_project.backend_api.appuser import AppUser
from hcm_project.backend_api.models.custom_user_model import Department
from hcm_project.backend_api.serializers import DepartmentSerializer, EmployeeSerializer

class DepartmentEmployeeList(APIView):
    def get(self, request):
        departments = Department.objects.all()
        data = []

        for department in departments:
            department_data = {
                'id': department.id,
                'name': department.name,
                'employees': []
            }

            employees = AppUser.objects.filter(department=department)
            employee_serializer = EmployeeSerializer(employees, many=True)
            
            department_data['employees'] = employee_serializer.data
            data.append(department_data)
        return Response(data, status=status.HTTP_200_OK)
    