from django.http import JsonResponse
from .models import ChargingPoint
from .serializers import ChargingSerializer

# Endpoints
def charging_list(request):
    charging = ChargingPoint.objects.all()
    serializer = ChargingSerializer(charging, many = True)
    return JsonResponse(serializer.data, safe = False)