# Generated by Django 3.0.3 on 2020-04-02 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('abone', '0004_auto_20200402_1600'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscriberaddresscreate',
            old_name='subscriber',
            new_name='subscriber_ID',
        ),
    ]
