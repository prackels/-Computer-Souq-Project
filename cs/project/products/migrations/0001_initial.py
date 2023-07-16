# Generated by Django 4.1 on 2023-05-10 15:55

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='new',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Brand', models.CharField(choices=[('HP', 'HP'), ('DELL', 'DELL'), ('LENOVO', 'LENOVO'), ('ACER', 'ACER'), ('ASUS', 'ASUS'), ('MSI', 'MSI'), ('HUAWEI', 'HUAWEI'), ('INFINIX', 'INFINIX'), ('OTHER', 'OTHER')], max_length=50)),
                ('Model', models.CharField(max_length=50, unique=True)),
                ('CPU', models.CharField(max_length=30)),
                ('Ram_Memory_Type', models.CharField(choices=[('DDR4', 'DDR4'), ('DDR5', 'DDR5')], max_length=30)),
                ('Ram_Memory_Size', models.IntegerField()),
                ('HD_Type', models.CharField(choices=[('SSD', 'SSD'), ('HDD', 'HDD')], max_length=30)),
                ('HD_Storage', models.IntegerField()),
                ('HD_Type_Other', models.CharField(blank=True, choices=[('SSD', 'SSD'), ('HDD', 'HDD')], max_length=30, null=True)),
                ('HD_Storage_Other', models.IntegerField(blank=True, null=True)),
                ('GPU', models.CharField(max_length=30)),
                ('Screen_Size', models.CharField(choices=[('11.6 inch', '11.6 inch'), ('12.5 inch', '12.5 inch'), ('13.3 inch', '13.3 inch'), ('14 inch', '14 inch'), ('15.6 inch', '15.6 inch'), ('17.3 inch', '17.3 inch')], max_length=30)),
                ('Screen_Resulation', models.CharField(choices=[('HD', 'HD'), ('FHD', 'FHD'), ('2K', '2K'), ('3K', '3K'), ('4K', '4K')], max_length=20)),
                ('Price', models.IntegerField()),
                ('Image', models.ImageField(upload_to='project/new/%y/%m/%d')),
                ('Description', models.TextField()),
                ('DateTime', models.DateTimeField(default=datetime.datetime(2023, 5, 10, 18, 54, 59, 264817))),
                ('Active', models.BooleanField(default=False)),
                ('Active_Home', models.BooleanField(default=False)),
                ('Quantity', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
            ],
        ),
        migrations.CreateModel(
            name='ram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Brand', models.CharField(default='Unknown', max_length=50)),
                ('Condition', models.CharField(choices=[('New', 'New'), ('Used', 'Used')], max_length=50)),
                ('Type', models.CharField(choices=[('DDR4', 'DDR4'), ('DDR5', 'DDR5')], max_length=20)),
                ('Size', models.IntegerField(choices=[('4', '4'), ('8', '8'), ('16', '16'), ('32', '32'), ('64', '64')])),
                ('Speed', models.IntegerField()),
                ('Quantity', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000)])),
                ('Price', models.IntegerField()),
                ('Available', models.BooleanField(default=True)),
                ('DateTime', models.DateTimeField(default=datetime.datetime(2023, 5, 10, 18, 54, 59, 264817))),
            ],
        ),
        migrations.CreateModel(
            name='used',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Brand', models.CharField(choices=[('HP', 'HP'), ('DELL', 'DELL'), ('LENOVO', 'LENOVO'), ('ACER', 'ACER'), ('ASUS', 'ASUS'), ('HUAWEI', 'HUAWEI'), ('SAMSUNG', 'SAMSUNG'), ('TOSHIBA', 'TOSHIBA'), ('SONY', 'SONY'), ('FUJITSU', 'FUJITSU')], max_length=50)),
                ('Model', models.CharField(max_length=50)),
                ('CPU', models.CharField(max_length=30)),
                ('Ram_Memory_Type', models.CharField(choices=[('DDR3', 'DDR3'), ('DDR3L', 'DDR3L'), ('DDR4', 'DDR4'), ('DDR5', 'DDR5')], max_length=30)),
                ('Ram_Memory_Size', models.IntegerField()),
                ('HD_Type', models.CharField(choices=[('SSD', 'SSD'), ('HDD', 'HDD')], max_length=30)),
                ('HD_Storage', models.IntegerField()),
                ('HD_Type_Other', models.CharField(blank=True, choices=[('SSD', 'SSD'), ('HDD', 'HDD')], max_length=30, null=True)),
                ('HD_Storage_Other', models.IntegerField(blank=True, null=True)),
                ('GPU', models.CharField(max_length=30)),
                ('Screen_Size', models.CharField(choices=[('11.6 inch', '11.6 inch'), ('12.5 inch', '12.5 inch'), ('13.3 inch', '13.3 inch'), ('14 inch', '14 inch'), ('15.6 inch', '15.6 inch'), ('17.3 inch', '17.3 inch')], max_length=30)),
                ('Screen_Resulation', models.CharField(choices=[('HD', 'HD'), ('FHD', 'FHD'), ('2K', '2K'), ('3K', '3K'), ('4K', '4K')], max_length=20)),
                ('Price', models.IntegerField()),
                ('Image', models.ImageField(upload_to='project/used/%y/%m/%d')),
                ('Description', models.TextField()),
                ('DateTime', models.DateTimeField(default=datetime.datetime(2023, 5, 10, 18, 54, 59, 264817))),
                ('Active', models.BooleanField(default=False)),
                ('Active_Home', models.BooleanField(default=False)),
                ('Quantity', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
            ],
        ),
    ]
