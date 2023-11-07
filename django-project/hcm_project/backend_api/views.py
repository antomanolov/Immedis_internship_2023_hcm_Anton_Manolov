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

# register and login
class RegisterView(generics.CreateAPIView):
    def create(self, request, *args, **kwargs):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else: 
            return Response({'not-valid': 'Not valid'}, status=status.HTTP_400_BAD_REQUEST)

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


# get the user and use it as AUTH for every page
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_logged_user_info(request):
    user = request.user
    user_info = {
        'email': user.email,
        'name': user.get_full_name(),
        'id': user.pk,
    }
    
    return Response(user_info, status=status.HTTP_200_OK)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_user_info(request, pk):
    
    try:
        user = AppUser.objects.get(pk=pk)

        data = {
            'user_name': user.get_full_name(),
            'department': user.department.name,
            'job_title': user.job_title.title,
            'firs_name': user.first_name,
            'last_name': user.last_name,
            'seniority': user.seniority,
            'location': user.location,
            'email': user.email,
            'telephone': user.telephone_number,
            'birthdate': user.date_of_birth,
            'gender': user.gender,
            'hire_date': user.date_of_hire,
        }
        return Response(data, status=status.HTTP_200_OK)
    except AppUser.DoesNotExist:
        return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

# logout and revoke the token of current user
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION')
    if auth_header and auth_header.startswith('Token '):
        token = auth_header[len('Token '):]
        try:
            user_auth_token = Token.objects.get(key=token)
            user_auth_token.delete()
            return Response({'message': 'Token has been revoked'}, status=status.HTTP_200_OK) 
        except Token.DoesNotExist:
            return Response({'message':'No token to revoke'}, status=status.HTTP_400_BAD_REQUEST)
    return Response({'message':'Invalid or missing auth token'}, status=status.HTTP_400_BAD_REQUEST)



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
    
    


