# Generated by Django 3.0.3 on 2020-04-07 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stok', '0003_auto_20200407_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory_device',
            name='gsm_brand',
            field=models.CharField(choices=[('', '---------'), ('turkcell', 'Turkcell'), ('vodafone', 'Vodafone'), ('turktelekom', 'Türk Telekom')], default=('', '---------'), max_length=20, null=True, verbose_name='Gsm Markası:'),
        ),
    ]
