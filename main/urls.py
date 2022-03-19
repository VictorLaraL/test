from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DeviceViewSet

router = DefaultRouter()
router.register(r'device', DeviceViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
