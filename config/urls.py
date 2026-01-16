from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from carcollect.views import CarViewSet

router = DefaultRouter()
router.register(r'cars', CarViewSet, basename='car')

urlpatterns = [
    path('admin/', admin.site.urls), # Garde ton admin existant
    path('api/', include(router.urls)),   # L'API sera sur /api/cars/
]