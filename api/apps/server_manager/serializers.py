from rest_framework import serializers
from .models import SimpleSSHConnector, ServerConfig



class SimpleSSHConnectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = SimpleSSHConnector
        fields = ["connection_ip", "connection_port", "ssh_username", "server_config"]


class SimpleSSHConnectorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SimpleSSHConnector
        fields = ('connection_ip',)


class ServerConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServerConfig
        fields = ('id', 'server_name', 'server_settings')


class ServerConfigListSerializer(serializers.ModelSerializer):
    ip =  serializers.IPAddressField(read_only=True, source="connector.connection_ip")
    port =  serializers.IntegerField(read_only=True, source="connector.connection_port")
    is_connected =  serializers.IntegerField(read_only=True, source="connector.is_connected")
    class Meta:
        model = ServerConfig
        fields = ('id', 'server_name', "ip", "port", "is_connected")
