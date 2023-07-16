from django.urls import path 
from . import views
urlpatterns = [
    path('', views.management, name='management'),
    ### STOCK ###
    path('newlaptopssheet', views.newlaptopsstock, name= 'newlaptopsstock'),
    path('usedlaptopsstock', views.usedlaptopsstock, name= 'usedlaptopsstock'),
    path('ramsstock', views.rams, name= 'ramsstock'),
    path('hardsstock', views.hardsstock, name= 'hardsstock'),
    # path('stock/ views.stock, name= 'stock'),
    ### INVOICES ###
    path('invoicesfromstock/', views.invoicesfromstock, name='invoicesfromstock'),
    path('invoicesfromstock/newinvoice/', views.new_invoice, name= 'newinvoice'),
    path('invoicesfromstock/newinvoice/newinvoiceview/<int:invoice_id>/', views.new_invoice_view, name='newinvoiceview'),
    path('invoicesfromstock/usedinvoice/', views.used_invoice, name= 'usedinvoice'),
    path('invoicesfromstock/usedinvoice/usedinvoiceview/<int:invoice_id>/', views.used_invoice_view, name='usedinvoiceview'),
    ### PRODUCTS FROM OUT SIDE ###
    
    
    
    ### ADD PRODUCTS ###
    path('addproducts', views.addproducts, name='addproducts'),
    
    ### PROFITS ###
    
    
    
]