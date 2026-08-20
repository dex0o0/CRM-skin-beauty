from django.contrib import admin
from .models import Client

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone', 'email', 'skin_type', 'created_at')
    search_fields = ('first_name', 'last_name', 'phone', 'email')
    list_filter = ('skin_type', 'created_at')
    ordering = ('-created_at',)
