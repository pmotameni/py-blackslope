from django.apps import AppConfig


class ApiAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apiapp"

    def ready(self) -> None:
        # use import to let signal find the models
        from apiapp.repositories.movies import Movie

        return super().ready()
