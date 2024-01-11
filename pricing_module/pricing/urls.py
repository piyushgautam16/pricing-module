# pricing/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import CalculatePricingViewSet
from .views import (
    pricing_form,
    PricingConfigListView,
    PricingConfigDetailView,
    PricingConfigFormView,
    activate_pricing_config,
    deactivate_pricing_config,
    delete_pricing_config,
)

router = DefaultRouter()
router.register(r'calculate-pricing', CalculatePricingViewSet, basename='calculate_pricing')

app_name = 'pricing'
urlpatterns = [
    path('', include(router.urls)),
    path('pricing-form/', pricing_form, name='pricing_form'),
    path('list/', PricingConfigListView.as_view(), name='pricing_config_list'),
    path('<int:pk>/', PricingConfigDetailView.as_view(), name='pricing_config_detail'),
    path('add/', PricingConfigFormView.as_view(), name='add_pricing_config'),
    path('edit/<int:pk>/', PricingConfigFormView.as_view(), name='edit_pricing_config'),
    path('activate/<int:pk>/', activate_pricing_config, name='activate_pricing_config'),
    path('deactivate/<int:pk>/', deactivate_pricing_config, name='deactivate_pricing_config'),
    path('delete-pricing-config/<int:pk>/', delete_pricing_config, name='delete_pricing_config'),
]
