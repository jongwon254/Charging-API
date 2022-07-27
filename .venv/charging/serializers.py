from rest_framework import serializers
from .models import ChargingPoint

# To JSON object
class ChargingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChargingPoint
        fields = ['id', 'operator', 'street', 'house_number', 'zip_code', 'city', 'power', 'number_ports']