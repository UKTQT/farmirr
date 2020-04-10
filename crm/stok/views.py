from django.shortcuts import render,redirect
from django.db.models import Q
from django.db.models import F
from .models import inventory_device
from .forms import CihazAra
from .forms import CihazEkle
from django.http import HttpResponse
from django.http import HttpResponseRedirect

# Create your views here.
def stokDetay(request):
    if 'devicedeletestock' in request.POST:
        devicedeleteid = request.POST.get('devicedeletestock')
        devicedelete = inventory_device.objects.get(pk = devicedeleteid)
        devicedelete.delete()
        return redirect('/stok')

    if 'deviceupdatestock' in request.POST:
        deviceupdateid = request.POST.get('device_id')
        deviceupdategsm_brand = request.POST.get('gsm_brand')
        deviceupdatedevice_type = request.POST.get('device_type')
        deviceupdatedb = inventory_device.objects.filter(
            Q(device_id=deviceupdateid))
        for devicee in deviceupdatedb:
            deviceupdate  = devicee.device_type
        if deviceupdate != deviceupdatedevice_type:
            inventory_device.objects.filter(device_id=deviceupdateid).update(device_type=deviceupdatedevice_type)
            return redirect('/stok')

    if 'stockid' in request.POST:
        stockdetailid = request.POST.get('stockid')
        stokcihazdetay = inventory_device.objects.filter(
            Q(device_id=stockdetailid))
        stokid = stokcihazdetay
    else:
        stokid = ""
    return render(request, "stok/stokdetay.html", {"form": stokid})


def index(request):
    if 'stoktümü' in request.POST:
        if request.user.has_perm('stok.add_inventory_device'):
            if request.user.seller_id != None:  # yani bayi ise
                device = inventory_device.objects.filter(
                    Q(seller_id=request.user.seller_id)
                )
                devicebilgi = device
            else:
                devicebilgi = inventory_device.objects.all()

    if 'stokara' in request.POST:
        deviceid = request.POST.get('device_id')
        devicetype = request.POST.get('device_type')
        gsmbrand = request.POST.get('gsm_brand')
        kullaniciid = request.user.seller_id

        if request.user.has_perm('stok.add_inventory_device'):
            if request.user.seller_id != 0:  # yani bayi ise

                devicefind = inventory_device.objects.filter(
                    Q(gsm_brand=gsmbrand) | Q(device_id=deviceid) | Q(device_type=devicetype))

                device = inventory_device.objects.filter(
                    Q(seller_id=request.user.seller_id) & Q(device_id=devicefind.device_id))
#todo buraya bak arama yapmıyor
                devicebilgi = device
                print(devicebilgi)
            else:  # normal kullanıcı
                devicebilgi = inventory_device.objects.all()

    else:
        if request.user.has_perm('stok.add_inventory_device'):
            if request.user.seller_id != None:  # yani bayi ise
                device = inventory_device.objects.filter(
                    Q(seller_id=request.user.seller_id)
                )
                devicebilgi = device
            else:
                devicebilgi = inventory_device.objects.all()

    return render(request, "stok/base.html", {'form': devicebilgi})



def cihazekle(request):
    #return render(request, "stok/cihazekle.html")
    if 'adddevice' in request.POST:

        form = CihazEkle(request.POST)
        if form.is_valid():
            cihaz_ekle = form.save(commit=False)
            cihaz_ekle.author = request.user
            cihaz_ekle.save()
            form = CihazEkle()
            return redirect('/stok')
    else:
        form = CihazEkle()
    return render(request, 'stok/cihazekle.html', {'form': form})




def stoksatisyonlendirme(request):
    if 'devicesell' in request.POST:
        deviceidsell = request.POST.get('devicesell')
        print(deviceidsell)
        cihazsellerid = request.POST.get('cihazsellerid')
        print(cihazsellerid)
        inventory_device.objects.filter(device_id=deviceidsell).update(seller_id=cihazsellerid)

    nulldeviceid = inventory_device.objects.filter(Q(seller_id=None))
    nulldevice = nulldeviceid

    return render(request, 'stok/satis_yonlendirme.html', {'form': nulldevice})


def stokcikis(request):
    alldevice = inventory_device.objects.all()
    return render(request, 'stok/stokcikis.html', {'form': alldevice})



