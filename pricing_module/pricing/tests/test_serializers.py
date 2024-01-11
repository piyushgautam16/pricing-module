from decimal import Decimal
from datetime import datetime, timezone
from django.test import TestCase
from django.core.exceptions import ValidationError
from rest_framework.test import APITestCase
from rest_framework import status
from ..models import PricingConfig
from ..serializers import PricingConfigSerializer

class PricingConfigSerializerTest(TestCase):
    def assertTimestampAlmostEqual(self, timestamp1, timestamp2):
        timestamp1_utc = datetime.fromisoformat(timestamp1.replace('Z', '+00:00')).replace(tzinfo=timezone.utc)
        timestamp2_utc = datetime.fromisoformat(timestamp2.replace('Z', '+00:00')).replace(tzinfo=timezone.utc)
        time_difference = abs((timestamp1_utc - timestamp2_utc).total_seconds())
        self.assertLessEqual(time_difference, 1)


    def test_pricing_config_serializer(self):
        pricing_config_data = {
            'name': 'Test Config',
            'is_active': True,
            'distance_base_price': 80,
            'distance_additional_price': 30,
            'time_multiplier_factor': 1.25,
            'waiting_charges': 5
            # Include other fields based on your model
        }
        pricing_config = PricingConfig.objects.create(**pricing_config_data)

        # Serialize the PricingConfig instance
        serializer = PricingConfigSerializer(instance=pricing_config)

        # Ensure the serialized data matches the expected structure and values
        expected_data = {
            'id': pricing_config.id,
            'name': 'Test Config',
            'is_active': True,
            'distance_base_price': '80.00',
            'distance_additional_price': '30.00',
            'time_multiplier_factor': '1.25',
            'waiting_charges': '5.00',
            'created_at': pricing_config.created_at.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z',
            # Include other fields based on your model
        }

        # Check if the serialized data matches the expected serialized data
        self.assertEqual(serializer.data['id'], expected_data['id'])
        self.assertEqual(serializer.data['name'], expected_data['name'])
        self.assertEqual(serializer.data['is_active'], expected_data['is_active'])
        self.assertEqual(serializer.data['distance_base_price'], expected_data['distance_base_price'])
        self.assertEqual(serializer.data['distance_additional_price'], expected_data['distance_additional_price'])
        self.assertEqual(serializer.data['time_multiplier_factor'], expected_data['time_multiplier_factor'])
        self.assertEqual(serializer.data['waiting_charges'], expected_data['waiting_charges'])

        # Check if 'created_at' is a substring of the expected format
        self.assertTimestampAlmostEqual(serializer.data['created_at'], expected_data['created_at'])

    def test_pricing_config_deserialization(self):
        # Create data to deserialize
        serialized_data = {
            'name': 'New Config',
            'is_active': False,
            'distance_base_price': '90.00',
            'distance_additional_price': '25.00',
            'time_multiplier_factor': '1.5',
            'waiting_charges': '7.00',
            'created_at': '2024-01-10T19:54:08.660Z',  # Adjusted timestamp format
            # Include other fields based on your model
        }

        # Deserialize the data
        serializer = PricingConfigSerializer(data=serialized_data)
        self.assertTrue(serializer.is_valid())

        # Save the deserialized data to create a new PricingConfig instance
        deserialized_instance = serializer.save()

        # Ensure the deserialized instance matches the expected values
        self.assertEqual(deserialized_instance.name, 'New Config')
        self.assertEqual(deserialized_instance.is_active, False)  # Ensure is_active is False
        # Include checks for other fields

        # Optionally, you can check if the serialized representation matches the original data
        self.assertEqual(serializer.data['is_active'], False)  # Ensure 'is_active' is False in serialized data
        # Include other checks for fields