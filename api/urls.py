from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('servers/', include('api.apps.server_manager.urls')),
]
