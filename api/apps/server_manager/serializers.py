from rest_framework import serializers
from .models import SimpleSSHConnector, ServerConfig, BaseConnector, KeySSHConnector


class SimpleSSHConnectorSerializer(serializers.ModelSerializer):

    class Meta:
        model = SimpleSSHConnector
        fields = '__all__'


class KeySSHConnectorSerializer(serializers.ModelSerializer):

    class Meta:
        model = KeySSHConnector
        exclude = ['polymorphic_ctype']


class SSHConnectorSerializer(serializers.ModelSerializer):
    #base_connector = BaseSSHConnectorSerializer

    class Meta:
        model = BaseConnector
        exclude = ['polymorphic_ctype']

    def to_representation(self, obj):
        if isinstance(obj, SimpleSSHConnector):
            return SimpleSSHConnectorSerializer(obj, context=self.context).to_representation(obj)
        elif isinstance(obj, KeySSHConnector):
            return KeySSHConnectorSerializer(obj, context=self.context).to_representation(obj)
        else:
            raise Exception('Unexpected type of tagged object')


class ServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServerConfig
        fields = ('id', 'server_name', 'is_connected', 'server_settings')


class ServerListSerializer(serializers.ModelSerializer):
    connector = SSHConnectorSerializer(read_only=True)

    class Meta:
        model = ServerConfig
        exclude = ['server_settings', ]
