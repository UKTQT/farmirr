# Generated by Django 3.0.3 on 2020-04-07 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='inventory_device',
            fields=[
                ('device_id', models.CharField(max_length=11, primary_key=True, serialize=False, unique=True, verbose_name='Cihaz ID:')),
                ('device_type', models.CharField(choices=[('ws', 'Hava Sensörü'), ('ss', 'Toprak Sensörü'), ('ps', 'Basınç Sensörü'), ('ps2', 'Basınç Sensörü 2'), ('wc', 'Kuyu merkezi')], max_length=20, verbose_name='Cihaz Tipi:')),
                ('gsm_brand', models.CharField(choices=[('turkcell', 'Turkcell'), ('vodafone', 'Vodafone'), ('turktelekom', 'Türk Telekom')], default=('vodafone', 'Vodafone'), max_length=20, verbose_name='Gsm Markası:')),
                ('date_of_entry', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
