# Generated by Django 4.1 on 2023-05-17 12:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0019_remove_invoice_new_branch_alter_invoice_new_datetime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice_new',
            name='DateTime',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 17, 15, 47, 47, 96295)),
        ),
        migrations.AlterField(
            model_name='invoice_used',
            name='DateTime',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 17, 15, 47, 47, 96295)),
        ),
    ]
