from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CarViewSet

# On utilise le router de DRF pour créer automatiquement les routes de l'API
router = DefaultRouter()
router.register(r'cars', CarViewSet, basename='car')

urlpatterns = [
    path('', include(router.urls)),
]