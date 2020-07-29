from django.contrib import admin
from .models import ServerConfig, SimpleSSHConnector, BaseConnection


@admin.register(ServerConfig)
class ServerAdmin(admin.ModelAdmin):
    list_display = ['server_name']


@admin.register(SimpleSSHConnector)
class SimpleSSHConnectionAdmin(admin.ModelAdmin):
    list_display = ['ssh_username']


@admin.register(BaseConnection)
class BaseConnectionAdmin(admin.ModelAdmin):
    list_display = ["connection_ip", "connection_port", "server_config",]