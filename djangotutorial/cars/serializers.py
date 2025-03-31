from rest_framework import serializers
from cars.models import Car

class CarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = [
            'id', 'make', 'model', 'year', 'price', 'mileage', 
            'body_type', 'cylinders', 'transmission', 'fuel_type', 
            'color', 'location', 'description'
        ]