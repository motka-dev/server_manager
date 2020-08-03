from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import SimpleSSHConnector, ServerConfig
from .serializers import ServerListSerializer


# class SimpleSSHConnectionCreate(ListAPIView):
#     queryset = SimpleSSHConnector.objects.all()
#     serializer_class = SimpleSSHConnectorSerializer


class ServerViewSet(ViewSet):
    def retrieve(self, request, pk=None):
        queryset = ServerConfig.objects.all()
        server = get_object_or_404(queryset, pk=pk)
        serializer = ServerSerializer(server)
        return Response(serializer.data)

    def list(self, request):
        queryset = ServerConfig.objects.all()
        serializer = ServerListSerializer(queryset, many=True)
        return Response(serializer.data)
