from django.urls import include, path

from hcm_project_frontend.bff_api.views import get_departments, LoginView, get_job_titles


urlpatterns = [
    path('api/', include([
        path('departments/', get_departments, name='all departments and employees in them api'),
        path('job-titles/', get_job_titles, name='job titles api'),
        path('login/', LoginView.as_view(), name='login api'),
    ]))
]
