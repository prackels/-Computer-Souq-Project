# Generated by Django 4.1 on 2023-05-10 21:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0009_alter_invoice_new_datetime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice_new',
            name='DateTime',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 11, 0, 19, 27, 534083)),
        ),
        migrations.DeleteModel(
            name='invoice_used',
        ),
    ]
