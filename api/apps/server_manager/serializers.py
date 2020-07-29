from rest_framework import serializers
from .models import SimpleSSHConnector, ServerConfig



class SimpleSSHConnectorSerializer(serializers.ModelSerializer):

    class Meta:
        model = SimpleSSHConnector
        fields = ('server_ip', 'ssh_username', 'server_ref', )



class SimpleSSHConnectorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SimpleSSHConnector
        fields = ('server_ip',)


class ServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServerConfig
        fields = ('id', 'server_name', 'is_connected', 'server_settings')