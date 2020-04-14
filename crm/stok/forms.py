from django import forms
from .models import inventory_device,paketkural


class CihazEkle(forms.ModelForm):
    class Meta:
        model = inventory_device
        fields = [
             'device_type',
            'gsm_brand',
        ]

    def __init__(self, *args, **kwargs):
        super(CihazEkle, self).__init__(*args, **kwargs)
        self.fields['device_type'].widget.attrs\
            .update({
                'id': 'device_type',

            })


class CihazAra(forms.ModelForm):
    class Meta:
        model = inventory_device
        fields = [

        ]


class PaketEkle(forms.ModelForm):
    class Meta:
        model = paketkural
        fields = [

        ]