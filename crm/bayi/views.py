from django.shortcuts import render,redirect
from .models import seller
from .models import selleraddress
from .forms import BayiEkle
from .forms import BayiAdres
import random
import sys
from django.db.models import Q
from django.contrib.auth.models import User
from  account.models import Profile
from django.contrib.auth.models import Permission


# Create your views here.
def index(request):
    if 'bayitümü' in request.POST:
        context = seller.objects.all()

    if 'bayiara' in request.POST:
        sellerid = request.POST.get('seller_id')
        sellername = request.POST.get('seller_name')
        telefonno = request.POST.get('phone_number')
        if (sellerid == "" and sellername == "" and telefonno == ""):
            context = seller.objects.all()
        sellerid = seller.objects.filter(
            Q(seller_id=sellerid) | Q(seller_name=sellername) | Q(phone_number=telefonno))
        context = sellerid
    else:
        context = seller.objects.all()
    return render(request, "bayi/base.html", {'form': context})


def bayiDetay(request):
    if 'bayidetaypasif' in request.POST:
        bayidetaypasif = request.POST.get('bayidetaypasif')
        seller.objects.filter(seller_id=bayidetaypasif).update(status ='pasif')
        selleraddress.objects.filter(address_owner_id=bayidetaypasif).update(status='pasif')
        return redirect('/bayi')



    if 'bayidetayguncelle' in request.POST:
        bayiid = request.POST.get('bayidetayguncelle')
        seller_name = request.POST.get('seller_name')
        seller_kadi = request.POST.get('seller_kadi')
        tax_number = request.POST.get('tax_number')
        authority = request.POST.get('authority')
        phone_number = request.POST.get('phone_number')
        email_address = request.POST.get('email_address')
        password = request.POST.get('password')
        country = request.POST.get('country')
        city = request.POST.get('city')
        district = request.POST.get('district')
        village = request.POST.get('village')
        address = request.POST.get('address')

        seller.objects.filter(seller_id=bayiid).update(seller_kadi=seller_kadi,seller_name=seller_name, tax_number=tax_number,
                                                                      authority=authority, phone_number=phone_number,
                                                                      email_address=email_address,password=password)
        selleraddress.objects.filter(address_owner_id=bayiid).update(country=country, city=city,
                                                                                district=district, village=village,
                                                                                address=address)
        return redirect('/bayi')





    if 'sellerid' in request.POST:
        sellerid = request.POST.get('sellerid')
        print(sellerid)
        saticidetay = seller.objects.filter(Q(seller_id=sellerid))
        print(saticidetay)
        saticiadresdetay = selleraddress.objects.filter(
            Q(address_owner_id=sellerid))
    else:
        saticidetay = ""
        saticiadresdetay = ""
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
            sellerbilgi.status = 'aktif'
            sellerbilgi.save()

            selleruser = Profile.objects.create_user(seller_id=sellerbilgi.seller_id,username=sellerbilgi.seller_kadi,email=sellerbilgi.email_address,password=sellerbilgi.password)
            selleruser.is_superuser = False
            selleruser.is_staff = False
            aboneeklemeizni = Permission.objects.get(codename='add_subscribercreate')
            stokeklemeizni = Permission.objects.get(codename='add_inventory_device')
            teknikservisizni = Permission.objects.get(codename='add_inventory_device')
            selleruser.user_permissions.add(aboneeklemeizni)
            selleruser.user_permissions.add(stokeklemeizni)
            selleruser.save()
            form = BayiEkle()

        if form2.is_valid():
            selleradres = form2.save(commit=False)
            selleradres.address_owner_id = sellerbilgi.seller_id
            selleradres.status = 'aktif'
            selleradres.save()
            form2 = BayiAdres()
            return redirect('/bayi')
    else:
        form = BayiEkle()
        form2 = BayiAdres()
    return render(request,'bayi/bayiekle.html',{'form': form,'form2':form2})
