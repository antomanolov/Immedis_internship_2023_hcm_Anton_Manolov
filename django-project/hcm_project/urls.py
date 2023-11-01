
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

    path('', include('hcm_project.frontend_app.urls')),
    path('api/', include('hcm_project.backend_api.urls')),

]
