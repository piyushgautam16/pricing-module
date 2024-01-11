# forms.py
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from .models import PricingConfig

class PricingConfigForm(forms.ModelForm):
    class Meta:
        model = PricingConfig
        fields = '__all__'  

    def __init__(self, *args, **kwargs):
        super(PricingConfigForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            'name',
            'is_active',
            'distance_base_price',
            'distance_additional_price',
            'time_multiplier_factor',
            'waiting_charges',
            Submit('submit', 'Save')
        )