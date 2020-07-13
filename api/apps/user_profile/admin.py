from django.contrib import admin
from .models import CustomUser


@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_filter = list_display = [
        "email",
        "date_joined",
        "last_login",
        "is_staff",
        "is_active",
    ]
