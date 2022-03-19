from rest_framework import serializers
from .models import Device, TypeDevice, StatusDevice


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

class StatusDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusDevice
        fields = (
            "id",
            "status_device",
        )


class TypeDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeDevice
        fields = (
            "id",
            "type_device",
        )