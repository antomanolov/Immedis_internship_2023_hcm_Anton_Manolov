import json
from django.http import JsonResponse
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# get deps and job titles 
def get_departments(request):
    backend_url = 'http://localhost:8000/api/core/departments/'
    response = requests.get(backend_url)
    
    if response.status_code == 200:
        data = response.json()
        return JsonResponse(data, safe=False)
    return JsonResponse({"error": "Failed to fetch employee data from the backend API."}, status=403)


def get_job_titles(request):
    backend_url = 'http://localhost:8000/api/core/job-titles/'
    response = requests.get(backend_url, headers=request.headers)

    if response.status_code == 200:
        data = response.json()
        return JsonResponse(data, safe=False)
    
    return JsonResponse({"error": "Failed to fetch employee data from the backend API."}, status=403)


# fetch the current logged user info
def get_current_user(request):
    backend_url = 'http://localhost:8000/api/core/get-user/'
    response = requests.get(backend_url, headers=request.headers)
    
    if response.status_code == 200:
        data = response.json()
        return JsonResponse(data=data, safe=False)
    return JsonResponse({"error": "Failed to fetch employee data from the backend API."}, status=403)



# fetch the wanted user info for profile view/edit/delete purposes
def get_user(request):
    backend_url = f'http://localhost:8000/api/core/user-by-id/{request.headers.get("Search-User-ID")}/'
    response = requests.get(backend_url, headers=request.headers)
    if response.status_code == 200:
        return JsonResponse(response.json(), status=200)
    return JsonResponse({"error": "Failed to fetch employee data from the backend API."}, status=403)    

# register/login/logout
class RegisterView(APIView):
    def post(self,request):
        backend_api_url = 'http://localhost:8000/api/core/create-employee/'  
        response = requests.post(backend_api_url, data=request.body, headers=request.headers)
        print(response.status_code)
        if response.status_code == 201:
            data = response.json()
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(data=response.json(), status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        data = request.data
        backend_api_url = 'http://localhost:8000/api/core/login/'  
        response = requests.post(backend_api_url, data=json.dumps(data), headers=request.headers)
        print(response.status_code)
        if response.status_code == 200:
            token = response.json().get('token')
            return Response({'token': token}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid email or password'}, status=status.HTTP_401_UNAUTHORIZED)

def logout_view(request):
    backend_url = 'http://localhost:8000/api/core/logout/'
    response = requests.post(backend_url, headers=request.headers)
    if response.status_code == 200:
        data = response.json()
        return JsonResponse(data=data, safe=False)
    return JsonResponse({"error": "Failed to fetch employee data from the backend API."}, status=403)

# edit/delete employee

def edit_user(request):
    print(request.user)
    backend_url = f'http://localhost:8000/api/core/update-user/{request.headers.get("Employee-id")}/'
    response = requests.patch(backend_url, data=request.body ,headers=request.headers)
    if response.status_code == 200:
        data = response.json()
        return JsonResponse(data=data, safe=False)
    return JsonResponse({"error": "Failed to fetch employee data from the backend API."}, status=403)

def delete_user(request):
    backend_url = f'http://localhost:8000/api/core/update-user/{request.headers.get("Employee-id")}/'
    response = requests.delete(backend_url, data=request.body ,headers=request.headers)
    if response.status_code == 200:
        data = response.json()
        return JsonResponse(data=data, safe=False)
    return JsonResponse({"error": "Failed to fetch employee data from the backend API."}, status=403)

# tasks/reviews/paychecks

def add_task(request):
    backend_url = f'http://localhost:8000/api/core/create-task/'
    response = requests.post(backend_url, data=request.body ,headers=request.headers)
    if response.status_code == 201:
        data = response.json()
        return JsonResponse(data=data, status=status.HTTP_201_CREATED)
    return JsonResponse({"error": "Failed to fetch employee data from the backend API."}, status=403)


def add_paycheck(request):
    backend_url = f'http://localhost:8000/api/core/create-paycheck/'
    response = requests.post(backend_url, data=request.body ,headers=request.headers)
    if response.status_code == 201:
        data = response.json()
        return JsonResponse(data=data, status=status.HTTP_201_CREATED)
    return JsonResponse({"error": "Failed to fetch employee data from the backend API."}, status=403)

def add_review(request):
    backend_url = f'http://localhost:8000/api/core/create-review/'
    response = requests.post(backend_url, data=request.body ,headers=request.headers)
    if response.status_code == 201:
        data = response.json()
        return JsonResponse(data=data, status=status.HTTP_201_CREATED)
    return JsonResponse({"error": "Failed to fetch employee data from the backend API."}, status=403)