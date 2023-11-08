from django.urls import include, path

from hcm_project.backend_api.views import DepartmentEmployeeList, JobTitlesList, LoginView, RegisterView, TasksCreate, UserProfileUpdateView, get_logged_user_info, get_user_info, logout


urlpatterns = [
    path('core/', include([
        path('get-user/',get_logged_user_info),
        path('user-by-id/<int:pk>/', get_user_info),
        path('update-user/<int:pk>/', UserProfileUpdateView.as_view()),
        
        path('departments/', DepartmentEmployeeList.as_view(), name='departments api'),
        path('job-titles/', JobTitlesList.as_view(), name='job titles api'),
        
        path('create-employee/', RegisterView.as_view(), name='register'),
        path('login/', LoginView.as_view(), name='login'),
        path('logout/', logout),
        
        path('create-task/', TasksCreate.as_view(), name='create task'),
        path('user-task/<int:pk>/', TasksCreate.as_view(), name='create task'),
    ])),

]
