# Generated by Django 3.0.3 on 2020-04-02 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('abone', '0002_auto_20200402_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriberaddresscreate',
            name='subscriber_ID',
            field=models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='abone.SubscriberCreate'),
        ),
    ]
