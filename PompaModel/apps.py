from django.apps import AppConfig


class PompamodelConfig(AppConfig):
    name = 'PompaModel'

    def ready(self):
        import PompaModel.signals
