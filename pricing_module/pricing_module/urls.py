# pricing_module/urls.py
from django.contrib import admin
from django.urls import path, include
from pricing.urls import urlpatterns as pricing_urls
from pricing.urls import router as pricing_router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pricing/', include('pricing.urls')),
    path('pricing/', include(pricing_router.urls)),
]
