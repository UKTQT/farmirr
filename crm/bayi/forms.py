from django import forms
from .models import seller
from .models import selleraddress


class BayiEkle(forms.ModelForm):
      class Meta:
            model = seller
            fields = [
                  'phone_number','seller_name',
                  'tax_number','authority',
                  'email_address','password',
            ]


class BayiAdres(forms.ModelForm):
    class Meta:
        model = selleraddress
        fields = [
            'country',
            'city', 'district',
            'village', 'address',
        ]