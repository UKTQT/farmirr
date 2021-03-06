from django.db import models

# Create your models here.
class seller(models.Model):
    seller_id = models.CharField(verbose_name='Id', primary_key=True, max_length=11)
    phone_number = models.CharField(max_length=11,verbose_name='Telefon No:')
    seller_name = models.CharField(max_length=50, verbose_name='Bayi Adı:')
    seller_kadi = models.CharField(max_length=50, verbose_name='Kullanıcı Adı:')
    tax_number = models.CharField(max_length=30, verbose_name='Vergi Numarası:')
    date_of_registration = models.DateTimeField(auto_now_add=True)
    status = models.CharField("Durum:", max_length=30, null=True)
    SELLER_AUTHORITY = [
            ('main_dealer', 'Ana Bayi'),
            ('normal_dealer', 'Normal Bayi'),
            ('suppliers', 'Tedarikçi'),
            ('main_dealer_employee', 'Ana Bayi Çalışanı'), ]
    authority = models.CharField(max_length=40, verbose_name='Yetki:',choices=SELLER_AUTHORITY)
    email_address = models.EmailField(verbose_name='E Mail:',max_length=40)
    password = models.CharField(max_length=16, verbose_name='Şifre:')

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
class selleraddress(models.Model):  # abone adres oluştur
    address_owner_id = models.CharField(max_length=11, primary_key=True)
    country = models.CharField(verbose_name="Ülke:", max_length=30, default='turkey')
    city = models.CharField(verbose_name="Şehir:", max_length=30, default=TURKEY_CITIES[4], choices=TURKEY_CITIES)
    district = models.CharField(verbose_name="Mahalle / Semt:", max_length=30)
    village = models.CharField(verbose_name="Köy / Kasaba:", max_length=30)
    address = models.TextField(verbose_name="Tam Adres:", max_length=128)
    status = models.CharField("Durum:", max_length=30, null=True)
    date_of_registration = models.DateTimeField(auto_now_add=True)
    date_of_update = models.DateTimeField(auto_now=True)
