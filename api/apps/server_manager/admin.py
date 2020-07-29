from django.contrib import admin
from .models import ServerConfig, SimpleSSHConnector


@admin.register(ServerConfig)
class ServerAdmin(admin.ModelAdmin):
    list_display = ['server_name', 'created', 'modificated']


@admin.register(SimpleSSHConnector)
class SimpleSSHConnectionAdmin(admin.ModelAdmin):
    list_display = ['ssh_username', 'connection_ip']


# @admin.register(BaseConnection)
# class BaseConnectionAdmin(admin.ModelAdmin):
#     list_display = ["connection_ip", "connection_port", "server_config",]