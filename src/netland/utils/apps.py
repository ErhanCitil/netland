from django.apps import AppConfig


class UtilsConfig(AppConfig):
    name = "netland.utils"

    def ready(self):
        from . import checks  # noqa
