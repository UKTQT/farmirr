from django.shortcuts import render
from .models import bildirim
from abone.models import SubscriberCreate
from abone.models import SubscriberAddressCreate
# Create your views here.

def index(request):
    if 'bildirimonayla' in request.POST:
        bildirimonayla = request.POST.get('bildirimonayla')
        bild = bildirim.objects.all()
        bildirim.objects.filter(bildirim_id=bildirimonayla).update(bildirim_durum='onaylandi')
        for bildirimm in bild:
            SubscriberCreate.objects.filter(subscriber_id=bildirimm.bildirim_subs_id).update(status='onaylandi')
            SubscriberAddressCreate.objects.filter(address_owner_id=bildirimm.bildirim_subs_id).update(status='onaylandi')

    bildirimler = bildirim.objects.all()
    return render(request, "bildirim/base.html",{'form':bildirimler})


