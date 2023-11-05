from django.urls import include, path

from hcm_project.backend_api.views import DepartmentEmployeeList, JobTitlesList, LoginView, RegisterView


urlpatterns = [
    path('core/', include([
        path('departments/', DepartmentEmployeeList.as_view(), name='departments api'),
        path('job-titles/', JobTitlesList.as_view(), name='job titles api'),
        path('create-employee/', RegisterView.as_view(), name='register'),
        path('login/', LoginView.as_view(), name='login'),
    ])),

]
