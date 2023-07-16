from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime
### Laptops Section ###
class used(models.Model):
    id = models.AutoField(primary_key=True)
    Brands = (
        ('HP', 'HP'),
        ('DELL', 'DELL'),
        ('LENOVO', 'LENOVO'),
        ('ACER', 'ACER'),
        ('ASUS', 'ASUS'),
        ('HUAWEI', 'HUAWEI'),
        ('SAMSUNG', 'SAMSUNG'),
        ('TOSHIBA', 'TOSHIBA'),
        ('SONY', 'SONY'),
        ('FUJITSU', 'FUJITSU'),
    )
    HD_Types = (
        ('SSD', 'SSD'),
        ('HDD', 'HDD'),
    )
    RAM_Type = (
        ('DDR3', 'DDR3'),
        ('DDR3L', 'DDR3L'),
        ('DDR4', 'DDR4'),
        ('DDR5', 'DDR5'),
    )
    Screen_Sizes = (
        ('11.6 inch', '11.6 inch'),
        ('12.5 inch', '12.5 inch'),
        ('13.3 inch', '13.3 inch'),
        ('14 inch', '14 inch'),
        ('15.6 inch', '15.6 inch'),
        ('17.3 inch', '17.3 inch'),
    )
    Screen_Resulations = (
        ('HD', 'HD'),
        ('FHD', 'FHD'),
        ('2K', '2K'),
        ('3K', '3K'),
        ('4K', '4K'),
    )
    Brand = models.CharField(max_length= 50, choices= Brands)
    Model = models.CharField(max_length= 50, unique=True)
    CPU = models.CharField(max_length=30)
    Ram_Memory_Type = models.CharField(max_length=30, choices= RAM_Type)
    Ram_Memory_Size = models.IntegerField()
    HD_Type = models.CharField(max_length=30, choices= HD_Types)
    HD_Storage = models.IntegerField()
    HD_Type_Other = models.CharField(max_length=30, choices= HD_Types, null= True, blank=True, default= 'HHD')
    HD_Storage_Other = models.IntegerField(null= True, blank=True)
    GPU = models.CharField(max_length=30)
    Screen_Size = models.CharField(max_length=30, choices= Screen_Sizes)
    Screen_Resulation = models.CharField(max_length=20, choices= Screen_Resulations)
    Cost = models.IntegerField()
    Price = models.IntegerField()
    Image = models.ImageField(upload_to='project/new/%y/%m/%d')
    Description = models.TextField(null= True, blank= True)
    DateTime = models.DateTimeField(default= datetime.now())
    Active = models.BooleanField(default= False)
    Active_Home = models.BooleanField(default= False)
    Quantity = models.IntegerField(default=1, validators=[MinValueValidator(0), MaxValueValidator(100)])
    
    def __str__(self):
        return f"{self.id}, {self.Brand} {self.Model}"
   
class new(models.Model):
    id = models.AutoField(primary_key=True)
    Brands = (
        ('HP', 'HP'),
        ('DELL', 'DELL'),
        ('LENOVO', 'LENOVO'),
        ('ACER', 'ACER'),
        ('ASUS', 'ASUS'),
        ('MSI', 'MSI'),
        ('HUAWEI', 'HUAWEI'),
        ('INFINIX', 'INFINIX'),
        ('OTHER', 'OTHER'),
     )
    HD_Types = (
         ('SSD', 'SSD'),
         ('HDD', 'HDD'),
     )
    RAM_Type = (
         ('DDR4', 'DDR4'),
         ('DDR5', 'DDR5'),
     )
    Screen_Sizes = (
         ('11.6 inch', '11.6 inch'),
         ('12.5 inch', '12.5 inch'),
         ('13.3 inch', '13.3 inch'),
         ('14 inch', '14 inch'),
         ('15.6 inch', '15.6 inch'),
         ('17.3 inch', '17.3 inch'),
     )
    Screen_Resulations = (
         ('HD', 'HD'),
         ('FHD', 'FHD'),
         ('2K', '2K'),
         ('3K', '3K'),
         ('4K', '4K'),
     )
    Brand = models.CharField(max_length= 50, choices= Brands)
    Model = models.CharField(max_length= 50, unique=True)
    CPU = models.CharField(max_length=30)
    Ram_Memory_Type = models.CharField(max_length=30, choices= RAM_Type)
    Ram_Memory_Size = models.IntegerField()
    HD_Type = models.CharField(max_length=30, choices= HD_Types)
    HD_Storage = models.IntegerField()
    HD_Type_Other = models.CharField(max_length=30, choices= HD_Types, null= True, blank=True, default= 'HHD')
    HD_Storage_Other = models.IntegerField(null= True, blank=True)
    GPU = models.CharField(max_length=30)
    Screen_Size = models.CharField(max_length=30, choices= Screen_Sizes)
    Screen_Resulation = models.CharField(max_length=20, choices= Screen_Resulations)
    Cost = models.IntegerField()
    Price = models.IntegerField()
    Image = models.ImageField(upload_to='project/new/%y/%m/%d')
    Description = models.TextField(null= True, blank= True)
    DateTime = models.DateTimeField(default= datetime.now())
    Active = models.BooleanField(default= False)
    Active_Home = models.BooleanField(default= False)
    Quantity = models.IntegerField(default=1, validators=[MinValueValidator(0), MaxValueValidator(100)])
    
    def __str__(self):
        return f"{self.id}, {self.Brand} {self.Model}"
#######################################################################################################################################
### RAM & Hard Disk Section ###
class ram(models.Model):
    id = models.AutoField(primary_key=True)
    RAM_Condition = (
        ('New', 'New'),
        ('Used', 'Used'),
    )
    RAM_Type = (
        ('DDR3', 'DDR3'),
        ('DDR3L', 'DDR3L'),
        ('DDR4', 'DDR4'),
        ('DDR5', 'DDR5'),
     )
    RAM_Size = (
        ('4', '4'),
        ('8', '8'),
        ('16', '16'),
        ('32', '32'),
        ('64', '64'),
    )
    Brand = models.CharField(max_length=50, default="Unknown")
    Condition = models.CharField(max_length=50,choices= RAM_Condition)
    Type = models.CharField(max_length=20, choices= RAM_Type)
    Size = models.CharField(max_length=100, choices= RAM_Size)
    Speed = models. IntegerField()
    Quantity = models.IntegerField(default=1, validators=[MinValueValidator(0), MaxValueValidator(1000)])
    Cost = models.IntegerField()
    Price = models.IntegerField()
    Available = models.BooleanField(default= True)
    DateTime = models.DateTimeField(default= datetime.now())
    Description = models.TextField(null= True, blank= True)


class hard(models.Model):
    id = models.AutoField(primary_key=True)
    Hard_Condition = (
        ('New', 'New'),
        ('Used', 'Used'),
    )
    Hard_Type = (
        ('HDD', 'HDD'),
        ('SSD SATA 2.5', 'SSD SATA 2.5'),
        ('SSD M.2', 'SSD M.2'),
        ('SSD NVMe', 'SSD NVMe'),
        ('SSD PCIe', 'SSD PCIe'),
    )
    Brand = models.CharField(max_length=50, default="Unknown")
    Condition = models.CharField(max_length=50, choices= Hard_Condition)
    Type = models.CharField(max_length=20, choices= Hard_Type)
    Size = models.IntegerField()
    Quantity = models.IntegerField(default=1, validators=[MinValueValidator(0), MaxValueValidator(10000)])
    Cost = models.IntegerField()
    Price = models.IntegerField()
    Available = models.BooleanField(default= True)
    DateTime = models.DateTimeField(default= datetime.now())
    Description = models.TextField(null= True, blank= True)

######################################################################################################################################
### Bags & Accessorys Section ###
class bag(models.Model):
    id = models.AutoField(primary_key=True)
    Sizes=(
        ('13-14 inch', '13-14 inch'),
        ('15-16 inch', '15-16 inch'),
        ('17-18 inch', '17-18 inch'),
    )
    Types=(
        ('Backpack', 'Backpack'),
        ('Shoulder', 'Shoulder'),
        ('Sleeve', 'Sleeve'),
        ('Other', 'Other'),
    )
    Brand= models.CharField(max_length=200)
    Type= models.CharField(max_length=50, choices=Types)
    Quantity = models.IntegerField(default=1, validators=[MinValueValidator(0), MaxValueValidator(10000)])
    Size = models.CharField(max_length=50, choices= Sizes)
    Cost = models.IntegerField()
    Price = models.IntegerField()
    Available = models.BooleanField(default= True)
    DateTime = models.DateTimeField(default= datetime.now())
    Description = models.TextField(null= True, blank= True)
    images = models.FileField()