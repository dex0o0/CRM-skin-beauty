from django.contrib import admin
from .models import Appointment

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('client', 'service', 'date', 'start_time', 'end_time', 'status', 'created_at')
    search_fields = ('client__first_name', 'client__last_name', 'service__name')
    list_filter = ('status', 'date', 'service')
    ordering = ('-date', '-start_time')
