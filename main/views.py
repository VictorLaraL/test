from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets, generics, status
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Binnacle, Device, StatusDevice, TypeDevice, Maintenance
from .serializers import (
    DeviceSerializer,
    StatusDeviceSerializer,
    TypeDeviceSerializer,
    BinnacleSerializer,
)
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone


class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["name"]
    pagination_class = PageNumberPagination

    def update(self, request, pk=None, *args, **kwargs): 
        try:
            if request.data.status_device == 2:
                actual_device = Device.objects.get(pk=pk)
                Maintenance.objects.create(device=actual_device, date=timezone.now())

            return super().update(request, *args, **kwargs)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        

    @action(detail=True, methods=["get"])
    def get_devices_by_type(self, request, pk=None, *args, **kwargs):
        try:
            instance = Device.objects.filter(type_device=pk)
        
            list_instances = []

            for record in instance:
                list_instances.append({
                    "id": record.id,
                    "name": record.name,
                    "type_device": record.type_device.type_device,
                    "actual_power":record.actual_power,
                    "status_device": record.status_device.status_device,
                    })
            
            return Response(list_instances)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        

class ListStatusDeviceViewSet(generics.ListAPIView):
    queryset = StatusDevice.objects.all()
    serializer_class = StatusDeviceSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    pagination_class = None


class ListTypeDeviceViewSet(generics.ListAPIView):
    queryset = TypeDevice.objects.all()
    serializer_class = TypeDeviceSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    pagination_class = None


class BinnacleViewSet(viewsets.ModelViewSet):
    queryset = Binnacle.objects.all()
    serializer_class = BinnacleSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["device__name", "date"]
    pagination_class = PageNumberPagination

    @action(detail=True, methods=["get"])
    def get_records_by_device(self, request, pk=None, *args, **kwargs):
        try:
            instance = Binnacle.objects.filter(device=pk)

            list_binnacle = []

            for record in instance:
                list_binnacle.appen({
                    "id":record.id,
                    "device": record.device.name,
                    "actual_power": record.actual_power,
                    "date":record.date,
                })

            return Response(list_binnacle)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=True, methods=["get"])
    def get_power_by_device(self, request, pk=None, *args, **kwargs):
        try:
            instance = Binnacle.objects.filter(device=pk)
            energy = 0

            for record in instance:
                energy += float(record.actual_power)

            return Response({
                "device": instance.device.name,
                "total_energy": energy,
            })
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)