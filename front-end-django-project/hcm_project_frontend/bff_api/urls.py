from django.urls import include, path

from hcm_project_frontend.bff_api.views import RegisterView, add_task, delete_user, edit_user, get_current_user, get_departments, LoginView, get_job_titles, get_user, logout_view


urlpatterns = [
    path('api/', include([
        #user related urls
        path('login/', LoginView.as_view()),
        path('logout/', logout_view),
        path('add-user/', RegisterView.as_view()),
        path('edit-user/', edit_user),
        path('delete-user/', delete_user),
        # work related urls
        path('departments/', get_departments),
        path('job-titles/', get_job_titles),
        path('add_task/', add_task),
        
        # helper urls
        path('current-user/', get_current_user),
        path('get-user/', get_user),
        
        
    ]))
]
