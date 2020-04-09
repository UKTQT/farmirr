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
        context = SubscriberCreate.objects.all()

    if 'kullanicitümü' in request.POST:
        context = SubscriberCreate.objects.all()

    return render(request, "abone/base.html", {"form": context})



def create():
    try:
        conn = psycopg2.connect("dbname='farmirr'user='postgres'host='127.0.0.1'password='ufuk123456'")
        print("Bağlanıldı")
    except:
        print("Bağlantı Hatası")
    subsCreateDay = time.strftime("%y" + "%m" + "%d")
    subscriberid = "SB" + subsCreateDay
    cur = conn.cursor()
    cur.execute("""SELECT subscriber_id FROM abone_subscribercreate ORDER BY subscriber_id DESC """)
    rows = cur.fetchall()
    cur.close()
    print(rows)
    lastid = rows[-1]
    print(lastid)
    cur.close()
    lastid = lastid[0]
    lastIdNumber = lastid[8:]
    print(lastIdNumber)
    lastIdDate = lastid[2:8]
    if not lastIdNumber:
        print("buna girdi")
        subscriberId = subscriberid + "001"
        return subscriberId
    if lastIdDate != subsCreateDay:
        print("bunagirdi")
        subscriberid = subscriberid + "001"
        return subscriberid
    else:
        print("buraya girdi")
        newid = str()
        if (int(lastIdNumber) + 1) < 10:
            print("son")
            newid = str(subscriberid + ("00" + (str(int(lastIdNumber) + 1))))
            print(newid)
        elif (int(lastIdNumber) + 1) >= 10:
            newid = str(subscriberid + ("0" + (str(int(lastIdNumber) + 1))))
            print(newid)
        elif (int(lastIdNumber) + 1) > 99:
            newid = str(subscriberid + str(int(lastIdNumber) + 1))
            print(newid)
        return newid



def aboneEkle(request):
    if request.method == 'POST':
        form = AboneEkle(request.POST)
        form2 = AboneEkle2(request.POST)
        id = create()
        if form.is_valid():
            kullanicibilgi = form.save(commit=False)
            rndid = random.randint(10000000000, 99999999999)
            print(rndid)
            kullanicibilgi.subscriber_id = rndid
            kullanicibilgi.user = request.user
            kullanicibilgi.save()
            print(rndid)

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



