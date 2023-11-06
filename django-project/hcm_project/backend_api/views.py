#DRF imports
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import authentication_classes, permission_classes, api_view
from rest_framework.permissions import IsAuthenticated


# generic models and imports from the app
from hcm_project.backend_api.appuser import AppUser
from hcm_project.backend_api.models.custom_user_model import Department, JobTitle
from hcm_project.backend_api.serializers import EmployeeSerializer, JobTitleSerializer, UserLoginSerializer

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_user_info(request):
    user = request.user
    user_info = {
        'email': user.email,
        'name': user.get_full_name(),
        'id': user.pk,
    }
    
    return Response(user_info, status=status.HTTP_200_OK)


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
    def create(self, request, *args, **kwargs):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        
        serializer = UserLoginSerializer(data=request.data, context={'request': request})
        
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })

