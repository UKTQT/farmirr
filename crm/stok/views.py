from django.shortcuts import render
from django.db.models import Q
from django.db.models import F
from .models import inventory_gsm
from .models import inventory_device
from .forms import GsmAra
from .forms import CihazAra
from .forms import GsmEkle
from .forms import CihazEkle

# Create your views here.
def gsmara(request):

    if request.method == 'POST':
        gsm_number = request.POST.get('gsm_number')
        #gsmid = inventory_gsm.objects.filter(gsm_number=F(gsm_number))
        gsmid = inventory_gsm.objects.filter(Q(gsm_number=gsm_number))
        gsmbilgi = gsmid
    else:
        gsmbilgi = GsmAra()
    return render(request, "stok/base.html", {'gsmbilgi': gsmbilgi})


def index(request):

    #return render(request, "stok/base.html")
    if request.method == 'POST':
        gsm_number = request.POST.get('gsm_number')
        # gsmid = inventory_gsm.objects.filter(gsm_number=F(gsm_number))
        if (gsm_number == None):
           gsmbilgi = inventory_gsm.objects.all()
        else:
            gsmid = inventory_gsm.objects.filter(Q(gsm_number=gsm_number))
            gsmbilgi = gsmid
#---------------------------------------------------------------------------
        deviceid = request.POST.get('device_id')
        devicetype = request.POST.get('device_type')
        if(deviceid == None and devicetype == None):
            devicebilgi = inventory_device.objects.all()
        else:
            device = inventory_device.objects.filter(Q(device_id=deviceid) | Q(device_type=devicetype))
            devicebilgi = device
    else:
        gsmbilgi = inventory_gsm.objects.all()
        devicebilgi = inventory_device.objects.all()
    return render(request, "stok/base.html", {'devicebilgi': devicebilgi,'gsmbilgi': gsmbilgi})




def gsmekle(request):
        if request.method == 'POST':
            form = GsmEkle(request.POST)

            if form.is_valid():
                gsm_ekle = form.save(commit=False)
                gsm_ekle.author = request.user
                gsm_ekle.save()

        else:
            form = GsmEkle()


        return render(request, 'stok/gsmekle.html', {'form': form})


def cihazekle(request):
    #return render(request, "stok/cihazekle.html")
    if request.method == 'POST':
        form = CihazEkle(request.POST)

        if form.is_valid():
            cihaz_ekle = form.save(commit=False)
            cihaz_ekle.author = request.user
            cihaz_ekle.save()

    else:
        form = CihazEkle()

    return render(request, 'stok/cihazekle.html', {'form': form})