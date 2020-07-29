from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import SimpleSSHConnectionCreate, ServerViewSet

router = SimpleRouter()

router.register('', ServerViewSet, basename='servers')
urlpatterns = [
    path('connectors/', SimpleSSHConnectionCreate.as_view()),
] + router.urls