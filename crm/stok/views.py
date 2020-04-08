from django.shortcuts import render
from django.db.models import Q
from django.db.models import F
from .models import inventory_device
from .forms import CihazAra
from .forms import CihazEkle

# Create your views here.
def stokDetay(request):
    if 'stockid' in request.POST:
        stockid = request.POST.get('stockid')
        print(stockid)

        stokcihazdetay = inventory_device.objects.filter(
            Q(device_id=stockid))
        stokid = stokcihazdetay
        return render(request, "stok/stokdetay.html", {"form": stokid})


def index(request):
    #return render(request, "stok/base.html")
    if request.method == 'POST':
        deviceid = request.POST.get('device_id')
        devicetype = request.POST.get('device_type')
        gsmbrand = request.POST.get('gsm_brand')

        if(deviceid == None and devicetype == None ):
            devicebilgi = inventory_device.objects.all()
        else:
            device = inventory_device.objects.filter(Q(gsm_brand=gsmbrand) | Q(device_id=deviceid) | Q(device_type=devicetype))
            devicebilgi = device
            print(devicebilgi)
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
    else:
        form = CihazEkle()
    return render(request, 'stok/cihazekle.html', {'form': form})



def stoksatisyonlendirme(request):

    nulldeviceid = inventory_device.objects.filter(Q(seller_id=""))
    nulldevice = nulldeviceid
    print(nulldevice)
    return render(request, 'stok/satis_yonlendirme.html', {'form': nulldevice})