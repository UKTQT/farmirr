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
        devicebilgi = inventory_device.objects.all()
    if 'stokara' in request.POST:
        deviceid = request.POST.get('device_id')
        devicetype = request.POST.get('device_type')
        gsmbrand = request.POST.get('gsm_brand')
        if(deviceid == None and devicetype == None ):
            devicebilgi = inventory_device.objects.all()
        else:
            device = inventory_device.objects.filter(Q(gsm_brand=gsmbrand) | Q(device_id=deviceid) | Q(device_type=devicetype))
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
    nulldeviceid = inventory_device.objects.filter(Q(seller_id="0"))
    nulldevice = nulldeviceid
    print(nulldevice)
    return render(request, 'stok/satis_yonlendirme.html', {'form': nulldevice})

def stokcikis(request):
    alldevice = inventory_device.objects.all()
    return render(request, 'stok/stokcikis.html', {'form': alldevice})