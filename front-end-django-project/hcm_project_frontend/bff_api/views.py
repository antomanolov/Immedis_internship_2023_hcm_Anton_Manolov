from django.http import JsonResponse
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

def get_departments(request):
    backend_url = 'http://localhost:8000/api/core/departments/'
    response = requests.get(backend_url)
    
    if response.status_code == 200:
        data = response.json()
        return JsonResponse(data, safe=False)
    
    return JsonResponse({"error": "Failed to fetch employee data from the backend API."}, status=403)


def get_job_titles(request):
    backend_url = 'http://localhost:8000/api/core/job-titles/'
    response = requests.get(backend_url)

    if response.status_code == 200:
        data = response.json()
        return JsonResponse(data, safe=False)
    
    return JsonResponse({"error": "Failed to fetch employee data from the backend API."}, status=403)


class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        
        
        backend_api_url = 'http://localhost:8000/api/core/login/'  # Replace with the actual URL of your Backend API login endpoint
        response = requests.post(backend_api_url, data={'email': email, 'password': password})

        if response.status_code == 200:
            token = response.json().get('token')
            return Response({'token': token}, status=status.HTTP_200_OK)
        else:
            
            return Response({'error': 'Invalid email or password'}, status=status.HTTP_401_UNAUTHORIZED)
