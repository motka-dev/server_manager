from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import SimpleSSHConnectionCreate, ServerConfigDetail

router = SimpleRouter()

router.register('', ServerConfigDetail, basename='servers')
urlpatterns = [
    #path('<int:pk>/', ServerConfigDetail),
] + router.urls