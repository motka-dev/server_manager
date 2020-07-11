from django.contrib import admin
from .models import ServerConnection, Server


@admin.register(Server)
class ServerAdmin(admin.ModelAdmin):
    list_display = ['server_ip', 'server_name']


@admin.register(ServerConnection)
class ServerConnectionAdmin(admin.ModelAdmin):
    list_display = ['ssh_username', 'ssh_password']
