from django.urls import include, path

from hcm_project.backend_api.views import DepartmentList, EmployeeListByDep


urlpatterns = [
    path('core/', include([
        path('departments/', DepartmentList.as_view(), name='departments list'),
        path('employees/', EmployeeListByDep.as_view(), name='employee list'),
        path('employees/<slug:department>/', EmployeeListByDep.as_view(), name ='employee list by dep')
    ])),

]
