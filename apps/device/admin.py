from django.contrib import admin
from .models import Device, DeviceCheckout, DeviceReturn
# Register your models here.
admin.site.register(Device)
admin.site.register(DeviceCheckout)
admin.site.register(DeviceReturn)
