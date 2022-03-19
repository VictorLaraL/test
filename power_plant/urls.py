from tracemalloc import Statistic
from django.contrib import admin
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

schema_view = get_schema_view(
    openapi.Info(
        title="Power Plant API",
        default_version='v1',
        description="API plantas electricas",
    ),
    public=True,
    permission_classes=(permissions.AllowAny, ),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include('main.urls')),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
