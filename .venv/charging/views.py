from .models import ChargingPoint
from .serializers import ChargingSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Endpoints

# endpoints for getting all charging points or creating one
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

# for requests with filter in URL
@api_view()
def charging_search(request):
    id = request.GET.get('id')
    param_operator = request.GET.get('operator')
    param_street = request.GET.get('street')
    param_house_number = request.GET.get('house_number')
    param_zip_code = request.GET.get('zip_code')
    param_city = request.GET.get('city')
    param_power = request.GET.get('power')
    param_ports = request.GET.get('ports')

    if  not param_power:
        charging = ChargingPoint.objects.filter(
        #pk=id, 
        #operator=param_operator,
        #street=param_street,
        #house_number=param_house_number,
        #zip_code=param_zip_code,
        city=param_city,
        #power=param_power,
        #number_ports=param_ports,
        )
    else:
        charging = ChargingPoint.objects.filter(
        #pk=id, 
        #operator=param_operator,
        #street=param_street,
        #house_number=param_house_number,
        #zip_code=param_zip_code,
        city=param_city,
        power=param_power,
        #number_ports=param_ports,
        )

    serializer = ChargingSerializer(charging, many=True)
    return Response(serializer.data)

# for requests with ID parameter in the URL
@api_view(['GET', 'PUT', 'DELETE'])
def charging_detail(request, id):

    # if given ID exists
    try:
        charging = ChargingPoint.objects.get(pk=id)
    except ChargingPoint.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # return requested charging point
    if request.method == 'GET':
        serializer = ChargingSerializer(charging)
        return Response(serializer.data)

    # update requested charging point
    elif request.method == 'PUT':
        serializer = ChargingSerializer(charging, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    # delete requested charging point
    elif request.method == 'DELETE':
        charging.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
