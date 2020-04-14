from django.shortcuts import render
from .models import bildirim
# Create your views here.

def index(request):
    if 'bildirimonayla' in request.POST:
        bildirimonayla = request.POST.get('bildirimonayla')
        bildirim.objects.filter(bildirim_id=bildirimonayla).update(bildirim_durum='onaylandi')

    bildirimler = bildirim.objects.all()
    return render(request, "bildirim/base.html",{'form':bildirimler})


