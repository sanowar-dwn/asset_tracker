from django.urls import path
from .import views

urlpatterns = [
    path('company-all', views.getCompanyData),
    path('employee-all', views.getEmployeeData),
    path('add-employee', views.addEmployee),
]
