from django.apps import AppConfig


class UserVendorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user_vendor'
    
    def ready(self):
            import user_vendor.signals