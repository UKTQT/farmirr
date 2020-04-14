# Generated by Django 3.0.3 on 2020-04-11 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stok', '0013_auto_20200411_1650'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paketkural',
            name='paket_kural',
        ),
        migrations.AddField(
            model_name='paketkural',
            name='basıncs',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='paketkural',
            name='havas',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='paketkural',
            name='kuyukontrol',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='paketkural',
            name='simkart',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='paketkural',
            name='topraks',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='paketkural',
            name='yazlisans',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='sellpaket',
            name='basıncs',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='sellpaket',
            name='havas',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='sellpaket',
            name='kuyukontrol',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='sellpaket',
            name='simkart',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='sellpaket',
            name='topraks',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='sellpaket',
            name='yazlisans',
            field=models.IntegerField(null=True),
        ),
    ]
