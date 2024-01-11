from django.test import TestCase
from ..forms import PricingConfigForm

class PricingConfigFormTest(TestCase):
    def test_valid_form(self):
        data = {
        'name': 'Test Config',
        'is_active': True,
        'distance_base_price': 80,
        'distance_additional_price': 30,
        'time_multiplier_factor': 1.25,
        'waiting_charges': 5,
        }
        form = PricingConfigForm(data=data)
        self.assertTrue(form.is_valid(), form.errors)

    def test_invalid_form(self):
        data = {'name': 'Test Config', 'is_active': True}  # Missing required field 'distance_base_price'
        form = PricingConfigForm(data=data)
        self.assertFalse(form.is_valid())
