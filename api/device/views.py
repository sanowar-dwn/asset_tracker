from rest_framework.response import Response
from rest_framework.decorators import api_view
from apps.device.models import Device
from .serializers import DeviceSerializer, DeviceCheckoutSerializer, DeviceReturnSerializer


@api_view(['GET'])
def getDeviceData(request):
    device_data_all = Device.objects.all()
    serializer = DeviceSerializer(device_data_all, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addDevice(request):
    serializer = DeviceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def checkoutDevice(request):
    serializer = DeviceCheckoutSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def checkoutDevice(request):
    serializer = DeviceCheckoutSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def returnDevice(request):
    serializer = DeviceReturnSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)