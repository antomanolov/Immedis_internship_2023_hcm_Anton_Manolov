#Django imports
from django.contrib.auth import login
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
from hcm_project.backend_api.models.app_models import Payroll, PerformanceReview, Task
from hcm_project.backend_api.models.custom_user_model import Department, JobTitle
from hcm_project.backend_api.serializers import EmployeeSerializer, JobTitleSerializer, PayrollSerializer, PerformanceReviewSerializer, TaskSerializer, UserLoginSerializer

# USER RELATED VIEWS

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
        if user is not None:
            login(request, user)

            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key,
                'user_id': user.pk,
                'email': user.email
            })
        return Response({'message': 'Invalid credentials'}, status=400)


class DepartmentEmployeeList(APIView):
    def get(self, request):
        # excluding the HRs becouse they are administration, and only the superuser will make changes to them
        # later cna be revisited
        departments = Department.objects.exclude(name='HR').all()
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


#get the info for any given user with pk(Primary key)
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_user_info(request, pk):
    try:
        user = AppUser.objects.get(pk=pk)

        data = {
            'id': user.pk,
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


# user update view and potentialy used for fetching get requests
# with user pk
class UserProfileUpdateView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        user_id = self.kwargs['pk']
        try:
            user = AppUser.objects.get(pk=user_id)
            return user
        except AppUser.DoesNotExist:
            return None
    
    def get(self, request, *args, **kwargs):
        user = AppUser.objects.get(pk=self.kwargs['pk'])
        serializer = self.serializer_class(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        user = self.get_object()

        if not user: 
            return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.serializer_class(
            user, data=request.data, partial=True
            )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, *args, **kwargs):
        user = self.get_object()
        
        if not user: 
            return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        
        user.delete()
        return Response({'message': 'User deleted successfully'}, status=status.HTTP_200_OK)
    

# OTHER VIEWS(TASKS/REVIEWS/PAYCHECKS)

class TasksCreate(generics.CreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
            # this method returns whatever keyword you put on the url
            # <int:pk> = self.kwargs['pk']
            user_pk = self.kwargs['pk']
            return Task.objects.filter(employee=user_pk)
    
    # this will be used to get all of the tasks for the user
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request, *args, **kwargs):
        creator_id = self.request.user.pk
        for_user_id = request.headers.get('For-User-ID')
        task_name = request.data.get('name')
        task_description = request.data.get('description')
        task_deadline = request.data.get('deadline')

        try:
            creator_user = AppUser.objects.get(pk=creator_id)
        except AppUser.DoesNotExist:
            return Response({'error': 'User not found.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            for_user = AppUser.objects.get(pk=for_user_id)
        except:
            return Response({'error': 'User not found.'}, status=status.HTTP_400_BAD_REQUEST)
        
        task_data = {
            'name': task_name,
            'description': task_description,
            'deadline': task_deadline,
            'employee': for_user.pk,
            'tasked_by': creator_user.pk,
        }

        serializer = self.serializer_class(data=task_data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PaycheckCreateView(generics.CreateAPIView):
    serializer_class = PayrollSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
            # this method returns whatever keyword you put on the url
            # <int:pk> = self.kwargs['pk']
            user_pk = self.kwargs['pk']
            return Payroll.objects.filter(employee=user_pk)
    
    # this will be used to get all of the tasks for the user
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request, *args, **kwargs):
        for_user_id = request.headers.get('For-User-ID')
        gross_salary = request.data.get('gross_salary')
        taxes = request.data.get('taxes')
        deductions = request.data.get('deductions')
        bonuses = request.data.get('bonuses')
        net_salary = request.data.get('net_salary')


        try:
            for_user = AppUser.objects.get(pk=for_user_id)
        except:
            return Response({'error': 'User not found.'}, status=status.HTTP_400_BAD_REQUEST)
        
        payroll_data = {
            'gross_salary': gross_salary,
            'taxes': taxes,
            'deductions': deductions,
            'bonuses': bonuses,
            'net_salary': net_salary,
            'day_of_monthly_payment': 1,
            'employee': for_user.pk,
        }

        serializer = self.serializer_class(data=payroll_data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PerformanceReviewView(generics.CreateAPIView):
    serializer_class = PerformanceReviewSerializer
    # permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
            # this method returns whatever keyword you put on the url
            # <int:pk> = self.kwargs['pk']
            user_pk = self.kwargs['pk']
            return PerformanceReview.objects.filter(employee=user_pk)
    
    # this will be used to get all of the tasks for the user
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request, *args, **kwargs):
        creator_id = self.request.user.pk
        for_user_id = request.headers.get('For-User-ID')
        review_points = request.data.get('review_points')
        feedback = request.data.get('feedback')
        goals_achieved = request.data.get('goals_achieved')
        improvement_areas = request.data.get('improvement_areas')


        try:
            creator_user = AppUser.objects.get(pk=creator_id)
        except AppUser.DoesNotExist:
            return Response({'error': 'User not found.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            for_user = AppUser.objects.get(pk=for_user_id)
        except:
            return Response({'error': 'User not found.'}, status=status.HTTP_400_BAD_REQUEST)
        
        review_data = {
            'review_points': review_points,
            'feedback': feedback,
            'goals_achieved': goals_achieved,
            'improvement_areas': improvement_areas,
            'employee': for_user.pk,
            'reviewed_by': creator_user.pk,
        }

        serializer = self.serializer_class(data=review_data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)