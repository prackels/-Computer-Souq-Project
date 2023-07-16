from django.contrib import admin
from .models import *
from products.models import *
class invoice_used_admin(admin.ModelAdmin):
    search_fields=['id']
class invoice_new_admin(admin.ModelAdmin):
    search_fields= ['id']
admin.site.register(invoice_used, invoice_used_admin)
admin.site.register(invoice_new, invoice_new_admin)