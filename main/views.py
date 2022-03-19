from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Device, TypeDevice
from .serializers import DeviceSerializer, TypeDeviceSerializer

class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name'] 
    pagination_class = PageNumberPagination
