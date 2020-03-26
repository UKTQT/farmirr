

# Register your models here.
from django.contrib import admin
from .models import SubscriberCreate
admin.site.register(SubscriberCreate)

from .models import SubscriberAddressCreate
admin.site.register(SubscriberAddressCreate)