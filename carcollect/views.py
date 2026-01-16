from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination
from .models import Car
from .serializers import CarSerializer

class CarPagination(PageNumberPagination):
    page_size = 6 # Nombre de voitures par page pour le front

class CarViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Car.objects.all().order_by('-year')
    serializer_class = CarSerializer
    pagination_class = CarPagination
    
    # Activation de la recherche (consigne : search)
    filter_backends = [filters.SearchFilter]
    search_fields = ['model', 'brand__name', 'category__name']