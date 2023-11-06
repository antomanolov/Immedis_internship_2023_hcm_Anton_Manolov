from django.urls import include, path

from hcm_project_frontend.bff_api.views import RegisterView, get_current_user, get_departments, LoginView, get_job_titles, logout_view


urlpatterns = [
    path('api/', include([
        path('departments/', get_departments),
        path('job-titles/', get_job_titles),
        path('add-user/', RegisterView.as_view()),
        path('login/', LoginView.as_view()),
        path('current-user/', get_current_user),
        path('logout/', logout_view),
    ]))
]
