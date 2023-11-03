from django.urls import include, path

from hcm_project.backend_api.views import DepartmentEmployeeList


urlpatterns = [
    path('core/', include([
        path('departments/', DepartmentEmployeeList.as_view(), name='departments list'),
        
    ])),

]
