from django import forms
from .models import inventory_device


class CihazEkle(forms.ModelForm):
    class Meta:
        model = inventory_device
        fields = [
            'device_id', 'device_type',
            'gsm_brand',
        ]


class CihazAra(forms.ModelForm):
    class Meta:
        model = inventory_device
        fields = [

        ]
