from django.urls import path
from .views import CreateInvoice, GetInvoiceStatus
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Standart API",
      default_version='v1',
      description="Тестовое задание API",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('create_invoice/', CreateInvoice.as_view(), name='create_invoice'),
    path('get_ivoice_status/<int:pk>', GetInvoiceStatus.as_view(), name='get_ivoice_status'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]