from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets, generics
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Device, StatusDevice, TypeDevice
from .serializers import DeviceSerializer, StatusDeviceSerializer, TypeDeviceSerializer
from rest_framework.response import Response

class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name'] 
    pagination_class = PageNumberPagination

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
