# Generated by Django 4.1 on 2023-05-13 03:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0014_rename_hard disk_invoice_new_harddisk_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice_new',
            name='DateTime',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 13, 6, 31, 59, 721377)),
        ),
        migrations.AlterField(
            model_name='invoice_used',
            name='DateTime',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 13, 6, 31, 59, 721377)),
        ),
    ]
