# Generated by Django 3.0.3 on 2020-04-11 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stok', '0011_auto_20200411_1607'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sellpaket',
            name='lisans',
        ),
    ]