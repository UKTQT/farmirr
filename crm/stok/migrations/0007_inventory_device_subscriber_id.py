# Generated by Django 3.0.3 on 2020-04-10 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stok', '0006_auto_20200410_0129'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory_device',
            name='subscriber_id',
            field=models.CharField(max_length=11, null=True),
        ),
    ]
