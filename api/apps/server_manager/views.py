from rest_framework.generics import (
    CreateAPIView, RetrieveUpdateDestroyAPIView,
)
from rest_framework.viewsets import ModelViewSet
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import SimpleSSHConnector, ServerConfig
from .serializers import SimpleSSHConnectorSerializer, ServerConfigSerializer, ServerConfigListSerializer


class SimpleSSHConnectionCreate(CreateModelMixin, UpdateModelMixin):
    pass



class ServerConfigDetail(ModelViewSet):
    queryset = ServerConfig.objects.all()
    serializer_class = ServerConfigSerializer

    def list(self, request):
        queryset = ServerConfig.objects.all()
        serializer_class = ServerConfigListSerializer(queryset, many=True)
        return Response(serializer_class.data)
