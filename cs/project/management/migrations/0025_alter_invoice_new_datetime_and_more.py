# Generated by Django 4.1 on 2023-05-19 19:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0025_alter_new_datetime_alter_ram_datetime_and_more'),
        ('management', '0024_rename_hard disk_invoice_used_harddisk_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice_new',
            name='DateTime',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 19, 22, 56, 40, 796206)),
        ),
        migrations.AlterField(
            model_name='invoice_used',
            name='DateTime',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 19, 22, 56, 40, 796206)),
        ),
        migrations.AlterField(
            model_name='invoice_used',
            name='Product_id',
            field=models.ManyToManyField(to='products.used'),
        ),
    ]