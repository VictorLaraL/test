from sqlite3 import Timestamp
from django.db import models


class Device(models.Model):
    name = models.CharField(max_length=150)
    type_device = models.ForeignKey("TypeDevice", on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    update_power = models.DateTimeField()
    actual_power = models.DecimalField(max_digits=19, decimal_places=10)
    status_device = models.ForeignKey("StatusDevice", on_delete=models.CASCADE)

    class Meta:
        ordering = ["name"]


class TypeDevice(models.Model):
    type_device = models.CharField(max_length=150)

    class Meta:
        ordering = ["type_device"]


class StatusDevice(models.Model):
    status_device = models.CharField(max_length=150)

    class Meta:
        ordering = ["status_device"]


class Reading(models.Model):
    device = models.ForeignKey("Device", on_delete=models.CASCADE)
    type_device = models.ForeignKey("TypeDevice", on_delete=models.CASCADE)
    actual_power = models.DecimalField(max_digits=19, decimal_places=10)
    timestamp = models.DateField()

    class Meta:
        ordering = ["device"]


class Binnacle(models.Model):
    device = models.ForeignKey("Device", on_delete=models.CASCADE)
    actual_power = models.DecimalField(max_digits=19, decimal_places=10)
    date = models.DateTimeField()

    class Meta:
        ordering = ["device"]

