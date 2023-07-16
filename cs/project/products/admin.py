from django.contrib import admin
from .models import *
class used_admin(admin.ModelAdmin):
    list_display= ['id' ,'Brand', 'Model', 'Quantity', 'Active', 'Active_Home']
    list_display_links= ['id', 'Brand']
    search_fields= ['Model', 'Brand']
    list_filter= ['DateTime'] 
    list_editable= ['Quantity', 'Active', 'Active_Home']
class new_admin(admin.ModelAdmin):
    list_display= ['id' ,'Brand', 'Model', 'Quantity', 'Active', 'Active_Home']
    search_fields= ['Model', 'Brand']
    list_filter= ['DateTime'] 
    list_editable= ['Quantity', 'Active', 'Active_Home']
class ram_admin(admin.ModelAdmin):
    list_display= ['Brand' ,'Type','Condition', 'Size', 'Speed', 'Cost', 'Price', 'Quantity', 'Available']
    list_editable = ['Available', 'Quantity']
class hard_admin(admin.ModelAdmin):
    list_display= ['Brand' ,'Type', 'Condition', 'Size', 'Cost', 'Price', 'Quantity', 'Available']
    list_editable = ['Available', 'Quantity']
class bag_admin(admin.ModelAdmin):
    list_display= ['Brand' ,'Type', 'Size', 'Cost', 'Price', 'Quantity', 'Available']
    list_editable = ['Available', 'Quantity']
admin.site.register(used, used_admin)
admin.site.register(new, new_admin)
admin.site.register(ram, ram_admin)
admin.site.register(hard, hard_admin)
admin.site.register(bag, bag_admin)