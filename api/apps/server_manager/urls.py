from django.contrib import admin
from django.urls import path, include
from .views import SSHConfig

urlpatterns = [
    path('servers/', SSHConfig),
]