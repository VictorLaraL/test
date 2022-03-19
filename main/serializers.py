from rest_framework import serializers
from .models import Device, TypeDevice, Binnacle


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = (
            "id",
            "name",
            "type_device",
            "start_date",
            "update_power",
            "actual_power",
            "status_device",
        )
