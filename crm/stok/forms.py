from django import forms
from .models import inventory_device
from .models import inventory_gsm


class GsmEkle(forms.ModelForm):
    class Meta:
        model = inventory_gsm
        fields = [
            'gsm_number', 'gsm_brand',
        ]

class CihazEkle(forms.ModelForm):
    class Meta:
        model = inventory_device
        fields = [
            'device_id', 'device_type',
            'parent_or_child'
        ]


class GsmAra(forms.ModelForm):
    class Meta:
        model = inventory_gsm
        fields = [

        ]

class CihazAra(forms.ModelForm):
    class Meta:
        model = inventory_device
        fields = [

        ]
