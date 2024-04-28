from django.urls import path
from .import views

urlpatterns = [
    path('', views.getCompanyData),
    path('add/', views.addCompany),
]
