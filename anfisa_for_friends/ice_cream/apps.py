from django.apps import AppConfig


class IceCreamConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ice_cream'
    # значение для локализации и отображаении в админке
    verbose_name = 'Каталог мороженого'
