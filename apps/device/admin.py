from django.contrib import admin
from .models import Device, DeviceCheckout, DeviceReturn
# Register your models here.
class DeviceAdmin(admin.ModelAdmin):
    list_display = ['name', 'company', 'is_checkedout']

admin.site.register(Device, DeviceAdmin)

class DeviceCheckoutAdmin(admin.ModelAdmin):
    list_display = ['device', 'employee', 'condition', 'date']

admin.site.register(DeviceCheckout, DeviceCheckoutAdmin)

class DeviceReturnAdmin(admin.ModelAdmin):
    list_display = ['device', 'employee', 'condition', 'date']

admin.site.register(DeviceReturn, DeviceReturnAdmin)
