from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from ..models import PricingConfig
from ..serializers import PricingConfigSerializer  # Import the serializer

class CalculatePricingAPITest(APITestCase):
    def setUp(self):
        self.active_config = PricingConfig.objects.create(
            name='Active Config',
            is_active=True,
            distance_base_price=80,
            distance_additional_price=30,
            time_multiplier_factor=1.25,
            waiting_charges=5
        )

    def test_calculate_pricing_api(self):
        url = '/pricing/calculate-pricing/'

        data = {'distance': 5, 'time': 2}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('price', response.data)

        data = {}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_calculate_pricing_no_active_config(self):
        self.active_config.is_active = False
        self.active_config.save()

        url = '/api/calculate-pricing/'

        data = {'distance': 5, 'time': 2}
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_calculate_pricing_with_serializer(self):
        url = '/pricing/calculate-pricing/'

        data = {'distance': 5, 'time': 2}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertIn('price', response.data)
        self.assertIn('config_data', response.data)

        serializer = PricingConfigSerializer(instance=self.active_config)
        self.assertEqual(response.data['config_data'], serializer.data)
