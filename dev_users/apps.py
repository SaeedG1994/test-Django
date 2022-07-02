from django.apps import AppConfig


class DevUsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dev_users'
    verbose_name = 'بخش پروفایل'

    def ready(self):
        import dev_users.signals