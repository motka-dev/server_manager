from django.contrib import admin
from .models import Server, SimpleSSHConnector, ConnectorType


@admin.register(Server)
class ServerAdmin(admin.ModelAdmin):
    list_display = ['server_name']


@admin.register(ConnectorType)
class ConnectorTypeAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(SimpleSSHConnector)
class SimpleSSHConnectionAdmin(admin.ModelAdmin):
    list_display = ['ssh_username', 'server_ip']
