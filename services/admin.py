from django.contrib import admin
from .models import Service

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'duration_minutes', 'category', 'is_active', 'created_at')
    search_fields = ('name', 'category')
    list_filter = ('category', 'is_active', 'created_at')
    ordering = ('-created_at',)
