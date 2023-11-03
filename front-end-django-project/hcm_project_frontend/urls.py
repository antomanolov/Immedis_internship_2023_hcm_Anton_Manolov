from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', include('hcm_project_frontend.frontend_app.urls')),
    path('bff/', include('hcm_project_frontend.bff_api.urls')),
]
