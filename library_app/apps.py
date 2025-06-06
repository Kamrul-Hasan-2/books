from django.apps import AppConfig


class LibraryAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'library_app'
    
    def ready(self):
        import library_app.signals  # Import signals
