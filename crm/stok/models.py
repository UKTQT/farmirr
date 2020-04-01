from django.db import models

# Create your models here.
class inventory_device(models.Model):
    device_id = models.CharField(verbose_name="Cihaz ID:",max_length=11, primary_key=True, unique=True,)
    ALL_DEVICE_TYPE = [
        ('ws', 'Hava Sensörü'),
        ('ss', 'Toprak Sensörü'),
        ('ps', 'Basınç Sensörü'),
        ('wc', 'Kuyu merkezi'),]
    device_type = models.CharField(verbose_name="Cihaz Tipi:",max_length=2, choices=ALL_DEVICE_TYPE)
    parent_or_child = models.BooleanField(verbose_name="Gsm Desteği Var mı ?:",)
    date_of_entry = models.DateTimeField(auto_now_add=True)



class inventory_gsm(models.Model):
    gsm_number = models.BigIntegerField(verbose_name="Gsm Numarası:",primary_key=True, unique=True)
    gsm_brand = models.CharField(verbose_name="Gsm Markası:",max_length=20)
    date_of_entry_ınv = models.DateTimeField(auto_now_add=True)
