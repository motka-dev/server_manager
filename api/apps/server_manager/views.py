from rest_framework.generics import CreateAPIView
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import SimpleSSHConnector, ServerConfig
from .serializers import SimpleSSHConnectorSerializer, ServerSerializer


class SimpleSSHConnectionCreate(CreateAPIView):
    queryset = SimpleSSHConnector.objects.all()
    serializer_class = SimpleSSHConnectorSerializer


class ServerViewSet(ViewSet):
    def retrieve(self, request, pk=None):
        queryset = ServerConfig.objects.all()
        server = get_object_or_404(queryset, pk=pk)
        serializer = ServerSerializer(server)
        return Response(serializer.data)
