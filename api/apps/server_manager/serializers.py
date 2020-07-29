from rest_framework import serializers
from .models import SimpleSSHConnector, Server



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
        model = Server
        fields = ('id', 'server_name', 'is_connected', 'server_settings')


class ServerListSerializer(serializers.ModelSerializer):
    connector = serializers.RelatedField()
    class Meta:
        model = Server
        fields = ('id', 'server_name', 'is_connected')

    def create(self, validated_data):
        server = Server.objects.create(
            server_name=validated_data['server_name'],
            is_connected=validated_data['is_connected']
            server_settings=validated_data['server_settings']
        )
        connector = SimpleSSHConnector.objects.get(pk=validated_data['connector'])
        SimpleSSHConnector.objects.create(server_ref=server, )