# Generated by Django 4.1 on 2023-05-10 15:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_alter_invoice_new_datetime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice_new',
            name='DateTime',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 10, 18, 57, 23, 152120)),
        ),
        migrations.AlterField(
            model_name='invoice_used',
            name='DateTime',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 10, 18, 57, 23, 152120)),
        ),
    ]
