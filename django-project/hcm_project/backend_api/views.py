from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password, check_password

from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from hcm_project.backend_api.appuser import AppUser
from hcm_project.backend_api.models.custom_user_model import Department, JobTitle
from hcm_project.backend_api.serializers import EmployeeSerializer, JobTitleSerializer

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

class JobTitlesList(APIView):
    def get(self, request):
        job_titles = JobTitle.objects.all()
        job_titles_serializer = JobTitleSerializer(job_titles, many=True)
        return Response(job_titles_serializer.data, status=status.HTTP_200_OK)
    
    

class RegisterView(generics.CreateAPIView):
    queryset = AppUser.objects.all()
    serializer_class = EmployeeSerializer


class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        raw_pass = request.data.get('password')
        print(raw_pass)
        
        # user = authenticate(request,username=email, password=password)
       
        # if user is not None:
        #     login(request, user)  # Login the user
        #     token = Token.objects.get_or_create(user=user)
        #     return Response({'token': token.key}, status=status.HTTP_200_OK)
        # else:
        return Response({'error': 'Invalid email or password'}, status=status.HTTP_401_UNAUTHORIZED)

