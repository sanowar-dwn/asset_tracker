from django.urls import path
from .import views

urlpatterns = [
    path('device-all', views.getDeviceData),
    path('add-device', views.addDevice),
    path('checkout-device', views.checkoutDevice),
    path('return-device', views.returnDevice),
]
