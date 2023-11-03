from django.http import HttpResponse, JsonResponse
import requests

def get_departments(request):
    backend_url = 'http://localhost:8000/api/core/departments/'
    response = requests.get(backend_url)
    
    if response.status_code == 200:
        data = response.json()
        return JsonResponse(data, safe=False)
    
    return JsonResponse({"error": "Failed to fetch employee data from the backend API."}, status=500)


