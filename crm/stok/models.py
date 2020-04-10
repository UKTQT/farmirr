from django.db import models

# Create your models here.
class inventory_device(models.Model):
    device_id = models.CharField(verbose_name="Cihaz ID:",max_length=11, primary_key=True, unique=True,)
    seller_id = models.CharField(null=True,verbose_name='Satıcı ID', max_length=11)
    subscriber_id = models.CharField(max_length=11, null=True)
    status = models.CharField(max_length=20,null=True)
    ALL_DEVICE_TYPE = [
        ('ws', 'Hava Sensörü'),
        ('ss', 'Toprak Sensörü'),
        ('ps', 'Basınç Sensörü'),
        ('ps2', 'Basınç Sensörü 2'),
        ('wc', 'Kuyu merkezi'),]
    device_type = models.CharField(verbose_name="Cihaz Tipi:",max_length=20, choices=ALL_DEVICE_TYPE)
    ALL_GSM_BRAND = [
        ('', '---------'),
        ('turkcell', 'Turkcell'),
        ('vodafone', 'Vodafone'),
        ('turktelekom', 'Türk Telekom'), ]
    gsm_brand = models.CharField(null=True, blank=True,default=ALL_GSM_BRAND[0],verbose_name="Gsm Markası:",choices=ALL_GSM_BRAND, max_length=20)
    date_of_entry = models.DateTimeField(auto_now_add=True)




