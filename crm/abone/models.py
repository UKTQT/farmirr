from django.db import models
from django_tables2 import tables

# Create your models here.
class SubscriberCreate(models.Model): #abone oluştur
    subscriber_id = models.CharField(max_length=11,primary_key=True) #abone id
    public_ID = models.CharField("Tc Kimlik No:",max_length=11, unique=True, null=False) #tckimlik
    seller_id = models.CharField("Bayi:", max_length=15, default=0)
    phone_number = models.CharField("Telefon No:",max_length=11, unique=True)
    email_address = models.EmailField("E-Posta:",max_length=40, unique=True)
    first_name = models.CharField("Ad:",max_length=15, null=False)
    last_name = models.CharField("Soyad:",max_length=20, null=False)
    date_of_registration = models.DateTimeField(auto_now_add=True)
    date_of_update = models.DateTimeField(auto_now=True)

TURKEY_CITIES = [
        ('1', 'ADANA'),
        ('2', 'ADIYAMAN'),
        ('3', 'AFYONKARAHİSAR'),
        ('4', 'AĞRI'),
        ('amasya', 'AMASYA'),
        ('6', 'ANKARA'),
        ('7', 'ANTALYA'),
        ('8', 'ARTVİN'),
        ('9', 'AYDIN'),
        ('10', 'BALIKESİR'),
        ('11', 'BİLECİKK'),
        ('12', 'BİNGÖL'),
        ('13', 'BİTLİS'),
        ('14', 'BOLU'),
        ('15', 'BURDUR'),
        ('16', 'BURSA'),
        ('17', 'ÇANAKKALE'),
        ('18', 'ÇANKIRI'),
        ('19', 'ÇORUM'),
        ('20', 'DENİZLİ'),
        ('21', 'DİYARBAKIR'),
        ('22', 'EDİRNE'),
        ('23', 'ELAZIĞ'),
        ('24', 'ERZİNCAN'),
        ('25', 'ERZURUM'),
        ('26', 'ESKİŞEHİR'),
        ('27', 'GAZİANTEP'),
        ('28', 'GİRESUN'),
        ('29', 'GÜMÜŞHANE'),
        ('30', 'HAKKARİ'),
        ('31', 'HATAY'),
        ('32', 'ISPARTA'),
        ('33', 'MERSİN'),
        ('34', 'İSTANBUL'),
        ('35', 'İZMİR'),
        ('36', 'KARS'),
        ('37', 'KASTAMONU'),
        ('38', 'KAYSERİ'),
        ('39', 'KIRKLARELİ'),
        ('40', 'KIRŞEHİR'),
        ('41', 'KOCAELİ'),
        ('42', 'KONYA'),
        ('43', 'KÜTAHYA'),
        ('44', 'MALATYA'),
        ('45', 'MANİSA'),
        ('46', 'KAHRAMANMARAŞ'),
        ('47', 'MARDİN'),
        ('48', 'MUĞLA'),
        ('49', 'MUŞ'),
        ('50', 'NEVŞEHİR'),
        ('51', 'NİĞDE'),
        ('52', 'ORDU'),
        ('53', 'RİZE'),
        ('54', 'SAKARYA'),
        ('55', 'SAMSUN'),
        ('56', 'SİİRT'),
        ('57', 'SİNOP'),
        ('58', 'SİVAS'),
        ('59', 'TEKİRDAĞ'),
        ('60', 'TOKAT'),
        ('61', 'TRABZON'),
        ('62', 'TUNCELİ'),
        ('63', 'ŞANLIURFA'),
        ('64', 'UŞAK'),
        ('65', 'VAN'),
        ('66', 'YOZGAT'),
        ('67', 'ZONGULDAK'),
        ('68', 'AKSARAY'),
        ('69', 'BAYBURT'),
        ('70', 'KARAMAN'),
        ('71', 'KIRIKKALE'),
        ('72', 'BATMAN'),
        ('73', 'ŞIRNAK'),
        ('74', 'BARTIN'),
        ('75', 'ARDAHAN'),
        ('76', 'IĞDIR'),
        ('77', 'YALOVA'),
        ('78', 'KARABÜK'),
        ('79', 'KİLİS'),
        ('80', 'OSMANİYE'),
        ('81', 'DÜZCE'),
        ]
class SubscriberAddressCreate(models.Model): #abone adres oluştur
    address_owner_id = models.CharField(max_length=11,primary_key=True)
    country = models.CharField(verbose_name="Ülke:",max_length=30, default='turkey')
    city = models.CharField(verbose_name="Şehir:",max_length=30,default=TURKEY_CITIES[4],choices=TURKEY_CITIES)
    district = models.CharField(verbose_name="Mahalle / Semt:",max_length=30)
    village = models.CharField(verbose_name="Köy / Kasaba:",max_length=30)
    address = models.TextField(verbose_name="Tam Adres:",max_length=128)
    date_of_registration = models.DateTimeField(auto_now_add=True)
    date_of_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.country

