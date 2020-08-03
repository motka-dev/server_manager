from django.contrib import admin
from .models import ServerConfig, SimpleSSHConnector, KeySSHConnector


@admin.register(ServerConfig)
class ServerConfigAdmin(admin.ModelAdmin):
    list_display = ['server_name']


@admin.register(SimpleSSHConnector)
class SimpleSSHConnectionAdmin(admin.ModelAdmin):
    list_display = ['connection_ip', 'connection_port', 'ssh_username']


@admin.register(KeySSHConnector)
class KeySSHConnectionAdmin(admin.ModelAdmin):
    list_display = ['connection_ip', 'connection_port', 'ssh_pubkey']
