# Generated by Django 4.2.1 on 2023-06-01 13:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0033_alter_invoice_new_datetime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice_new',
            name='DateTime',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 1, 16, 7, 42, 57904)),
        ),
        migrations.AlterField(
            model_name='invoice_used',
            name='DateTime',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 1, 16, 7, 42, 57904)),
        ),
    ]
