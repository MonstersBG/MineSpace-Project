from django.contrib import admin
from .models import AppUser


# Register your models here.

@admin.register(AppUser)
class AppUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'user_type', 'date_joined', 'last_login']
    list_filter = ['is_active', 'is_staff', 'is_superuser']

    def user_type(self, obj):
        if obj.is_staff:
            return 'Site Admin'
        return 'User'

    user_type.admin_order_field = 'is_superuser'

    ordering = ['-is_superuser', '-date_joined']
