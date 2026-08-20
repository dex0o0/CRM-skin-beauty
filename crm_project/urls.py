"""
URL configuration for crm_project project.
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from clients.views import ClientViewSet
from products.views import ProductViewSet
from services.views import ServiceViewSet
from appointments.views import AppointmentViewSet
from . import views

router = DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'products', ProductViewSet)
router.register(r'services', ServiceViewSet)
router.register(r'appointments', AppointmentViewSet)

urlpatterns = [
    path('', views.admin_custom, name='admin_custom'),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
