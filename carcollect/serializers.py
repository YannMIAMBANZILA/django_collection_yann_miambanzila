from rest_framework import serializers
from .models import Car

class CarSerializer(serializers.ModelSerializer):
    brand_name = serializers.ReadOnlyField(source='brand.name')
    category_name = serializers.ReadOnlyField(source='category.name')

    class Meta:
        model = Car
        fields = ['id', 'model', 'brand_name', 'category_name', 'year', 'price', 'power_hp']