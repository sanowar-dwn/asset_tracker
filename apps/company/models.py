from django.db import models
from  django.contrib.auth.models import User
# Create your models here.

class Company(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name.username


class Employee(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    employee = models.OneToOneField(User, on_delete=models.CASCADE)
    employee_number = models.IntegerField()

    def __str__(self):
        return self.employee.username