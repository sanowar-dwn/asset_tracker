from rest_framework import serializers
from apps.device.models import Device, DeviceCheckout, DeviceReturn

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'

class DeviceCheckoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceCheckout
        fields = '__all__'

class DeviceReturnSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceReturn
        fields = '__all__'