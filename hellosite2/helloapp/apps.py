from django.apps import AppConfig
from django.shortcuts import render


class HelloappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'helloapp'

