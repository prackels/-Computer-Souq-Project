# Generated by Django 4.1 on 2023-05-15 12:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_alter_new_datetime_alter_ram_datetime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='DateTime',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 15, 15, 56, 48, 538079)),
        ),
        migrations.AlterField(
            model_name='ram',
            name='DateTime',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 15, 15, 56, 48, 538079)),
        ),
        migrations.AlterField(
            model_name='used',
            name='DateTime',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 15, 15, 56, 48, 528610)),
        ),
    ]
