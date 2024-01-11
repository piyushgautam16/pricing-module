from django.test import TestCase
from ..models import PricingConfig

class PricingConfigModelTest(TestCase):
    def test_pricing_config_str_representation(self):
        pricing_config = PricingConfig.objects.create(
            name='Test Config',
            is_active=True,
            distance_base_price=100,
            distance_additional_price=30,
            time_multiplier_factor=1.25,
            waiting_charges=5)
        self.assertEqual(str(pricing_config), 'Test Config')
