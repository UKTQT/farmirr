# Generated by Django 3.0.3 on 2020-04-02 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('abone', '0007_auto_20200402_1633'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscriberaddresscreate',
            old_name='subscriber_ID',
            new_name='subscriber',
        ),
        migrations.RenameField(
            model_name='subscribercreate',
            old_name='subscriber_ID',
            new_name='subscriber_id',
        ),
    ]
