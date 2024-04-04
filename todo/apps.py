from django.apps import AppConfig
from . import db

class TodoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'todo'
    def ready(self):
        db.connect()