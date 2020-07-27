from rest_framework import viewsets
from rest_framework.response import Response


class SSHConfig(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    def retrieve(self, request, pk=None):
        return Response('ret')

    def post(self, request):
        #queryset = ServerConnection.objects.all()
        print(request)
        return Response('post')

    def get(self, request):
        print(request)
        return Response('get')
