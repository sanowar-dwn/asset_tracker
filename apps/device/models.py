from django.db import models
from ..company.models import Company, Employee
from django.core.exceptions import ValidationError

class Device(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    is_checkedout = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} {self.is_checkedout}"


class DeviceCheckout(models.Model):
    CONDITION_CHOICES = [
        ('GOOD', 'GOOD'),
        ('BAD', 'BAD')
    ]
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    condition = models.CharField(max_length=50, choices=CONDITION_CHOICES)
    date = models.DateTimeField(null=True, blank=True)

    def clean(self):
        if self.device.is_checkedout:
            raise ValidationError("This device is already checked out.")

    def save(self, *args, **kwargs):
        # Check if the device is not already checked out
        if not self.device.is_checkedout:
            # Update is_checkedout attribute
            self.device.is_checkedout = True
            # Save the updated device
            self.device.save()
        super().save(*args, **kwargs)

class DeviceReturn(models.Model):
    CONDITION_CHOICES = [
        ('GOOD', 'GOOD'),
        ('BAD', 'BAD')
    ]
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    condition = models.CharField(max_length=50, choices=CONDITION_CHOICES)
    date = models.DateTimeField(null=True, blank=True)

    def clean(self):
        if not self.device.is_checkedout:
            raise ValidationError("Device isn't checked out yet.")

    def save(self, *args, **kwargs):
        # Call clean method to perform validation
        self.clean()

        # Update is_checkedout attribute of the associated device
        self.device.is_checkedout = False

        # Save the updated device
        self.device.save()

        super().save(*args, **kwargs)

