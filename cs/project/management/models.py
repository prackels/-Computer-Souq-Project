from django.db import models    
from datetime import datetime
from products.models import *
from django.core.validators import MaxValueValidator, MinValueValidator

class invoice_new(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Phone = models.IntegerField()
    Product_id = models.ManyToManyField(new)
    Quantity = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(100)])
    Ram= models.IntegerField()
    HardDisk= models.CharField(max_length=50)
    HardDisk_Other= models.CharField(max_length=50, null= True, blank=True)
    SN= models.CharField(max_length=50, null= True, blank=True)
    Price = models.IntegerField()
    Branch = models.CharField(max_length=50)
    DateTime = models.DateTimeField(default= datetime.now())
    def __str__(self):
        return str(self.id)
    
class invoice_used(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Phone = models.IntegerField()
    Product_id = models.ManyToManyField(used)
    Quantity = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(100)])
    Ram= models.IntegerField()
    HardDisk= models.CharField(max_length=50)
    HardDisk_Other= models.CharField(max_length=50, null= True, blank=True)
    SN= models.CharField(max_length=50, null= True, blank=True)
    Price = models.IntegerField()
    Branch = models.CharField(max_length=50)
    DateTime = models.DateTimeField(default= datetime.now())
    def __str__(self):
        return str(self.id)
    
    
    
