from rest_framework import serializers
from chocolate.models import Sales

class ChocolateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sales
        fields = [
            'id', 'sales_person', 'country', 'product', 
            'date', 'amount', 'boxes_shipped'
        ]
