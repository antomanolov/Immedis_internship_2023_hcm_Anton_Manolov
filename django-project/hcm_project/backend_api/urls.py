from django.urls import include, path

from hcm_project.backend_api.views import DepartmentEmployeeList, JobTitlesList, LoginView, RegisterView, get_logged_user_info, get_user_info, logout


urlpatterns = [
    path('core/', include([
        path('get-user/',get_logged_user_info),
        path('user-by-id/<int:pk>/', get_user_info),
        path('departments/', DepartmentEmployeeList.as_view(), name='departments api'),
        path('job-titles/', JobTitlesList.as_view(), name='job titles api'),
        path('create-employee/', RegisterView.as_view(), name='register'),
        path('login/', LoginView.as_view(), name='login'),
        path('logout/', logout),
        
    ])),

]
