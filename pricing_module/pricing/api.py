from decimal import Decimal
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from .models import PricingConfig
from .serializers import PricingConfigSerializer

class CalculatePricingViewSet(viewsets.ViewSet):
    def create(self, request):

        active_config = PricingConfig.objects.filter(is_active=True).first()

        if not active_config:
            raise Http404("No active pricing configuration found.")

        distance = request.data.get('distance')
        time = request.data.get('time')

        if distance is None or time is None:
            return Response({'error': 'Both distance and time must be provided.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            distance = Decimal(distance)
            time = Decimal(time)
        except (ValueError, TypeError, InvalidOperation):
            return Response({'error': 'Invalid values for distance or time.'}, status=status.HTTP_400_BAD_REQUEST)

        calculated_price = (
            (active_config.distance_base_price + (distance * active_config.distance_additional_price)) +
            (time * Decimal(active_config.time_multiplier_factor)) +
            (time * active_config.waiting_charges)
        )

        serializer = PricingConfigSerializer(active_config)

        return Response({'price': calculated_price, 'config_data': serializer.data}, status=status.HTTP_200_OK)