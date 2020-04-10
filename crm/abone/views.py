from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.db.models import Q
from .forms import AboneEkle
from .forms import AboneEkle2
import random
import psycopg2
import time
from .models import SubscriberCreate
from .models import SubscriberAddressCreate
from django import forms
from django.shortcuts import render
from pytz import timezone
# Create your views here.
import datetime

def aboneDetay(request):
    if 'sbid' in request.POST:
        sbid = request.POST.get('sbid')
        kullanicidetay = SubscriberCreate.objects.filter(
            Q(subscriber_id=sbid))
        kullaniciadresdetay = SubscriberAddressCreate.objects.filter(
            Q(address_owner_id=sbid))
    else:
        kullanicidetay = ""
        kullaniciadresdetay = ""
    return render(request, "abone/abonedetay.html", {"form": kullanicidetay,"form2":kullaniciadresdetay})


def index(request):
    if 'kullaniciara' in request.POST:
        soyad = request.POST.get('last_name')
        try:
            tckimlik = request.POST['public_ID']
        except KeyError:
            tckimlik = None
        telefonno = request.POST.get('phone_number')


        if (soyad == "" and tckimlik == "" and telefonno == ""):
            form = SubscriberCreate.objects.all()

        kullaniciid = SubscriberCreate.objects.filter(
            Q(last_name=soyad) | Q(public_ID=tckimlik) | Q(phone_number=telefonno)
        )
        context = kullaniciid

    else:
        if request.user.has_perm('abone.add_subscribercreate'):
            if request.user.seller_id != None:
                kullaniciid = SubscriberCreate.objects.filter(
                    Q(seller_id=request.user.seller_id)
                )
                context = kullaniciid
            else:
                context = SubscriberCreate.objects.all()


    if 'kullanicitümü' in request.POST:
        if request.user.has_perm('abone.add_subscribercreate'):
            if request.user.seller_id != 0:
                kullaniciid = SubscriberCreate.objects.filter(
                    Q(seller_id=request.user.seller_id)
                )
                context = kullaniciid
            else:
                context = SubscriberCreate.objects.all()

    return render(request, "abone/base.html", {"form": context})



def aboneEkle(request):
    if request.method == 'POST':
        form = AboneEkle(request.POST)
        form2 = AboneEkle2(request.POST)

        if form.is_valid():
            kullanicibilgi = form.save(commit=False)
            rndid = random.randint(10000000000, 99999999999)
            kullanicibilgi.subscriber_id = rndid

            if request.user.has_perm('abone.add_subscribercreate'):
                if request.user.seller_id != None:
                    kullanicibilgi.seller_id = request.user.seller_id
                else:
                    kullanicibilgi.seller_id = '0'


            kullanicibilgi.user = request.user
            kullanicibilgi.save()


        if form2.is_valid():
            kullaniciadres = form2.save(commit=False)
            kullaniciadres.address_owner_id = kullanicibilgi.subscriber_id
            kullaniciadres.save()
            return redirect('/abone')

    else:
        form = AboneEkle()
        form2 = AboneEkle2()
    return render(request,'abone/aboneekle.html',{'form': form,'form2':form2})

#------------------------------------------------------------------------

def aboneAra(request):
    pass
    #return render(request, 'abone/base.html', {'form': form}) ***bu form mantığını araştır şu abone bitince



