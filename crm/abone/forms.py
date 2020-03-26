from django import forms
from .models import SubscriberCreate
from .models import SubscriberAddressCreate


class AboneEkle(forms.ModelForm):
      class Meta:
            model = SubscriberCreate
            fields = [
                  'first_name','last_name',
                  'public_ID','phone_number',
                  'email_address',
            ]

class AboneEkle2(forms.ModelForm):
      class Meta:
            model = SubscriberAddressCreate
            fields = [
                  'country',
                  'city','district',
                  'village','address',
            ]



class AboneAra(forms.ModelForm):
      class Meta:
            model = SubscriberCreate
            fields = [

            ]




