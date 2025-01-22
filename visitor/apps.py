from django.apps import AppConfig


class VisitorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'visitor'
    verbose_name = 'Informasaun Jeral'  # Custom label
    def ready(self):
        import visitor.signals