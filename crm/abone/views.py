from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.db.models import Q
from .forms import AboneEkle
from .forms import AboneEkle2
from .forms import AboneAra
from .models import SubscriberCreate
from django import forms
from django.db.models import F
from django.shortcuts import render
# Create your views here.

def index(request):
    pass

def aboneEkle(request):
    if request.method == 'POST':
        form = AboneEkle(request.POST)
        form2 = AboneEkle2(request.POST)

        if form.is_valid():
            kullanicibilgi = form.save(commit=False)
            kullanicibilgi.author = request.user
            kullanicibilgi.save()



# ADRES KISMI EKLENMİYOR BAK
        if form2.is_valid():
            kullaniciadres = form.save(commit=False)
            kullaniciadres.author = request.user
            kullaniciadres.save()

        if kullanicibilgi.save() and kullaniciadres.save():
            return HttpResponseRedirect('/abone/abonekle')

    else:
        form = AboneEkle()
        form2 = AboneEkle2()


    return render(request,'abone/aboneekle.html',{'form': form,'form2':form2})

#------------------------------------------------------------------------

def aboneAra(request):
    if request.method == 'POST':
        soyad = request.POST.get('last_name')

        try:
            tckimlik = request.POST['public_ID']
        except KeyError:
            tckimlik = None

        telefonno = request.POST.get('phone_number')

        kullaniciid = SubscriberCreate.objects.filter(
            Q(last_name=soyad) | Q(public_ID=tckimlik) | Q(phone_number=telefonno)
        )
        form = kullaniciid
        context = {
            "articl":kullaniciid
        }


     #   pass
        #form = AboneAra()
        #if form.is_valid():
        #a = SubscriberCreate.objects.filter(last_name=F('last_name'))
        #return HttpResponseRedirect('/abone/aboneara')
    else:
        form = AboneAra()

    return render(request, "abone/base.html", {'form': form})
    #return render(request, 'abone/base.html', {'form': form}) ***bu form mantığını araştır şu abone bitince
