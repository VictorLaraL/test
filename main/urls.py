from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DeviceViewSet, ListStatusDeviceViewSet, ListTypeDeviceViewSet

router = DefaultRouter()
router.register(r'device', DeviceViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/liststatus', ListStatusDeviceViewSet.as_view(), name="status_device"),
    path('api/listtype', ListTypeDeviceViewSet.as_view(), name="type_device"),
]
