from django.db import models

# Create your models here.

class bildirim(models.Model):
    bildirim_id = models.AutoField(primary_key=True)
    bildirim_icerik = models.CharField(max_length=500,null=True)
    bildirim_durum = models.CharField(max_length=30, null=True)
    bildirim_subs_id = models.CharField(max_length=30, null=True)