from rest_framework.generics import CreateAPIView
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import SimpleSSHConnector, Server
from .serializers import SimpleSSHConnectorSerializer, ServerSerializer, ServerListSerializer


class SimpleSSHConnectionCreate(CreateAPIView):
    queryset = SimpleSSHConnector.objects.all()
    serializer_class = SimpleSSHConnectorSerializer


class ServerViewSet(ViewSet):
    def retrieve(self, request, pk=None):
        queryset = Server.objects.all()
        server = get_object_or_404(queryset, pk=pk)
        serializer = ServerSerializer(server)
        return Response(serializer.data)

    def list(self, request):
        queryset = Server.objects.all()
        serializer = ServerListSerializer(queryset, many=True)
        return Response(serializer.data)


