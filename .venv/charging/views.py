from django.http import JsonResponse
from .models import ChargingPoint
from .serializers import ChargingSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Endpoints
@api_view(['GET', 'POST']) 
def charging_list(request):

    if request.method == 'GET':
        charging = ChargingPoint.objects.all()
        serializer = ChargingSerializer(charging, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = ChargingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def charging_detail(request, id):

    try:
        charging = ChargingPoint.objects.get(pk=id)
    except ChargingPoint.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ChargingSerializer(charging)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ChargingSerializer(charging, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        charging.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
