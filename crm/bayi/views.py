from django.shortcuts import render
from .models import seller
from .models import selleraddress
from .forms import BayiEkle
from .forms import BayiAdres
import random
from django.db.models import Q

# Create your views here.
def index(request):
    if request.method == 'POST':
        sellerid = request.POST.get('seller_id')
        sellername = request.POST.get('seller_name')
        telefonno = request.POST.get('phone_number')

        #try:
         #   tckimlik = request.POST['public_ID']
        #except KeyError:
         #   tckimlik = None

        if (sellerid == "" and sellername == "" and telefonno == ""):
            context = seller.objects.all()

        sellerid = seller.objects.filter(
            Q(seller_id=sellerid) | Q(seller_name=sellername) | Q(phone_number=telefonno)
        )

        context = sellerid

    else:
        context = seller.objects.all()

    return render(request, "bayi/base.html", {'form': context})

def bayiDetay(request):
    if 'sellerid' in request.POST:
        sellerid = request.POST.get('sellerid')
        print(sellerid)
        saticidetay = seller.objects.filter(Q(seller_id=sellerid))
        print(saticidetay)
        saticiadresdetay = selleraddress.objects.filter(
            Q(address_owner_id=sellerid))
        return render(request, "bayi/bayidetay.html", {"form": saticidetay, "form2": saticiadresdetay})


def bayiEkle(request):
    if request.method == 'POST':
        form = BayiEkle(request.POST)
        form2 = BayiAdres(request.POST)

        if form.is_valid():
            sellerbilgi = form.save(commit=False)
            rndid = random.randint(10000000000, 99999999999)
            print(rndid)
            sellerbilgi.seller_id = rndid
            sellerbilgi.user = request.user
            sellerbilgi.save()
            form = BayiEkle()

        if form2.is_valid():
            selleradres = form2.save(commit=False)
            selleradres.address_owner_id = sellerbilgi.seller_id
            selleradres.save()
            form2 = BayiAdres()
    else:
        form = BayiEkle()
        form2 = BayiAdres()
    return render(request,'bayi/bayiekle.html',{'form': form,'form2':form2})
