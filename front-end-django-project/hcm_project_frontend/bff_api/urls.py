from django.urls import include, path

from hcm_project_frontend.bff_api.views import get_departments


urlpatterns = [
    path('api/', include([
        path('departments/', get_departments, name='all departments'),
        
    ]))
]
