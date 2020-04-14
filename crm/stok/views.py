from django.shortcuts import render,redirect
from django.db.models import Q
from django.db.models import F
from .models import inventory_device,paketkural
from .forms import CihazAra
from .forms import CihazEkle
from abone.models import SubscriberCreate
from django.http import HttpResponse
from django.http import HttpResponseRedirect

# Create your views here.
def stokDetay(request):
    if 'devicedeletestock' in request.POST:
        devicedeleteid = request.POST.get('devicedeletestock')
        inventory_device.objects.filter(device_id=devicedeleteid).update(status ='pasif')
        return redirect('/stok')

    if 'deviceupdatestock' in request.POST:
        deviceupdateid = request.POST.get('deviceupdatestock')
        deviceupdate_gsm_brand = request.POST.get('gsm_brand')
        deviceupdate_device_type = request.POST.get('device_type')

        inventory_device.objects.filter(device_id=deviceupdateid).update(device_type=deviceupdate_device_type,gsm_brand=deviceupdate_gsm_brand)
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

        if request.user.has_perm('stok.add_inventory_device'): #cihaz ekleme yetkisi var mı ?

            if request.user.seller_id != None:  #bayi

                if gsmbrand == '':
                    print("gsm boş")
                    devicefind = inventory_device.objects.filter(
                         (Q(device_id=deviceid) | Q(device_type=devicetype)) & Q(seller_id=kullaniciid))
                    devicebilgi = devicefind


                elif gsmbrand != '':
                    print("gsm boş değil")
                    devicefind = inventory_device.objects.filter(
                        (Q(device_id=deviceid) | Q(gsm_brand=gsmbrand)) & Q(seller_id=kullaniciid))
                    devicebilgi = devicefind


                elif gsmbrand == '' and devicetype =='' and deviceid != '':
                    device = inventory_device.objects.filter(
                        Q(seller_id=kullaniciid) & Q(device_id=deviceid))
                    devicebilgi = device


            else:  # ---------------------   normal kullanıcı

                if gsmbrand == '':
                    print("gsm boş")
                    devicefind = inventory_device.objects.filter(
                         Q(device_id=deviceid) | Q(device_type=devicetype))
                    devicebilgi = devicefind


                elif gsmbrand != '':
                    print("gsm boş değil")
                    devicefind = inventory_device.objects.filter(
                        Q(device_id=deviceid) | Q(gsm_brand=gsmbrand))
                    devicebilgi = devicefind


                elif gsmbrand == '' and devicetype =='' and deviceid != '':
                    device = inventory_device.objects.filter(
                        Q(device_id=deviceid))
                    devicebilgi = device

    else:   # --- stok ara butonuna basılmadığı zaman
        if request.user.seller_id == None:  # normal kullanıcı
            devicebilgi = inventory_device.objects.all()
        else:   # Bayi
            device = inventory_device.objects.filter(
                Q(seller_id=request.user.seller_id)
            )
            devicebilgi = device

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
    if 'teklicihazaratümübuton' in request.POST:
        tekilboscihazgetir = inventory_device.objects.filter(Q(seller_id=None))
        tekilnulldevice = tekilboscihazgetir

    if 'teklicihazarabuton' in request.POST:
        tekilcihazgsm_brand = request.POST.get('tekilcihazgsm_brand')
        tekilcihazdevice_type = request.POST.get('tekilcihazdevice_type')
        if request.user.seller_id == "":
            if tekilcihazgsm_brand == "":
                tekilboscihazgetir = inventory_device.objects.filter(Q(device_type=tekilcihazdevice_type) & Q(seller_id=None))
                tekilnulldevice = tekilboscihazgetir
            else:
                tekilboscihazgetir = inventory_device.objects.filter(
                    Q(device_type=tekilcihazdevice_type) & Q(seller_id=None) & Q(gsm_brand=tekilcihazgsm_brand))
                tekilnulldevice = tekilboscihazgetir
        else:
            if tekilcihazgsm_brand == "":
                tekilboscihazgetir = inventory_device.objects.filter(Q(device_type=tekilcihazdevice_type) & Q(seller_id=request.user.seller_id))
                tekilnulldevice = tekilboscihazgetir
            else:
                tekilboscihazgetir = inventory_device.objects.filter(
                    Q(device_type=tekilcihazdevice_type) & Q(seller_id=request.user.seller_id) & Q(gsm_brand=tekilcihazgsm_brand))
                tekilnulldevice = tekilboscihazgetir
    else:
        if request.user.seller_id == "":
            tekilboscihazgetir = inventory_device.objects.filter(Q(seller_id=None))
            tekilnulldevice = tekilboscihazgetir
        else:
            tekilboscihazgetir = inventory_device.objects.filter(Q(seller_id=request.user.seller_id) & Q(subscriber_id=None))
            tekilnulldevice = tekilboscihazgetir


    # ------------------------------------------------------------------------------------------------------


    if 'tekilcihazsatisbuton' in request.POST:
        device_id = request.POST.get('tekilcihazsatisbuton')
        cihazsellerid = request.POST.get('cihazsellerid')
        cihazsubsid = request.POST.get('cihazsubsid')

        if request.user.seller_id == None:
            print("aaaaaaaaaaaaaaaaaa")
            if device_id == "" and cihazsellerid == "":
                pass
            elif cihazsellerid == "":
                pass
            elif cihazsellerid != "" and device_id != "":
                print(cihazsellerid)
                print(device_id)
                inventory_device.objects.filter(device_id=device_id).update(seller_id=cihazsellerid)

        else:
            print("wrtttttttttttt")
            if device_id == "" and cihazsubsid == "":
                pass
            elif cihazsubsid == "":
                pass
            elif cihazsubsid != "" and device_id != "":
                inventory_device.objects.filter(device_id=device_id).update(status='aktif',subscriber_id=cihazsubsid)


    sellersubsid = SubscriberCreate.objects.filter(seller_id=request.user.seller_id)
    print(sellersubsid)

    return render(request, 'stok/satis_yonlendirme.html', {'form': tekilnulldevice,'form2':sellersubsid})


def toplusatis(request):
    if 'toplucihaztümüabuton' in request.POST:   #----------TOPLU SATIŞ
        toplunulldevice = inventory_device.objects.filter(Q(seller_id=None))


    if 'toplucihazaraabuton' in request.POST:   #----------TOPLU SATIŞ
        toplucihazdevice_type = request.POST.get('toplucihazdevice_type')
        toplucihazgsm_brand =request.POST.get('toplucihazgsm_brand')

        if toplucihazgsm_brand == "":
            topluboscihazgetir = inventory_device.objects.filter(
                Q(device_type=toplucihazdevice_type) & Q(seller_id=None))
            toplunulldevice = topluboscihazgetir
        else:
            topluboscihazgetir = inventory_device.objects.filter(
                Q(device_type=toplucihazdevice_type) & Q(seller_id=None) & Q(gsm_brand=toplucihazgsm_brand))
            toplunulldevice = topluboscihazgetir
    else:
        toplunulldevice =  inventory_device.objects.filter(Q(seller_id=None))


    if 'toplucihazsatbuton' in request.POST:   #----------TOPLU SATIŞ
        toplusatisdeger1 = request.POST.get('toplusatisdeger1')
        toplusatisdeger2 =request.POST.get('toplusatisdeger2')
        toplusatisbayiid=request.POST.get('toplusatisbayiid')

        toplusatisdeger1int = int(toplusatisdeger1)
        toplusatisdeger2int = int(toplusatisdeger2)

        for x in range(toplusatisdeger1int,toplusatisdeger2int+1):
            print(x)
            inventory_device.objects.filter(Q(seller_id=None) & Q(device_id=int(x))).update(seller_id=toplusatisbayiid)



    return render(request, 'stok/toplusatis.html',{'form':toplunulldevice})




def paketsatis(request):
    return render(request, 'stok/paketsatis.html')


def stokcikis(request):

    return render(request, 'stok/stokcikis.html')


def paketekle(request):
    if 'addpacked' in request.POST:
        paketad = request.POST.get('paketad')
        topraks = request.POST.get('topraks')
        basinc = request.POST.get('basinc')
        havas = request.POST.get('havas')
        kksens = request.POST.get('kksens')
        sim = request.POST.get('sim')
        yazlisans = request.POST.get('yazlisans')
        paketkuralekle = paketkural(paket_ad=paketad, topraks=topraks, havas=havas, basıncs=basinc, kuyukontrol=kksens, simkart=sim, yazlisans=yazlisans)
        paketkuralekle.save()
        return redirect('/stok/paketekle')
    else:
        allpacket = paketkural.objects.all()
        return render(request, 'stok/paketekle.html', {'form': allpacket})

