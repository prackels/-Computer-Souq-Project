# Generated by Django 4.1 on 2023-05-10 15:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice_new',
            name='DateTime',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 10, 18, 55, 7, 453485)),
        ),
        migrations.AlterField(
            model_name='invoice_used',
            name='DateTime',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 10, 18, 55, 7, 453485)),
        ),
    ]
