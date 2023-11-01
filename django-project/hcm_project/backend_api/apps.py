from django.apps import AppConfig


class BackendApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'hcm_project.backend_api'
    
    def ready(self) -> None:
        import hcm_project.backend_api.signals
