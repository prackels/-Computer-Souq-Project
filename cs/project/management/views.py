from django.shortcuts import render
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseNotAllowed, HttpResponseRedirect
from requests import Response
from .models import *
from products.models import *
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
@login_required
def management(request):
    if not request.user.is_staff:
        return render(request, 'management/error.html')
    return render(request, 'management/management.html')


@login_required
def invoicesfromstock(request):
    if not request.user.is_staff:
        return render(request, 'management/error.html')
    return render(request, 'management/invoicesfromstock.html')
    
#######################################################################################################################################
### فواتير الجديد ###
@login_required
def new_invoice(request):
    if not request.user.is_staff:
        return render(request, 'management/error.html')
    if request.method == 'POST': # البوست المرفوع من ال FORM 
        product_id = request.POST.get('product_id')
        customer_name = request.POST.get('customer_name')
        customer_phone = request.POST.get('customer_phone')
        ram = request.POST.get('ram')
        hard = request.POST.get('hard')
        hard2=request.POST.get('hard2')
        quantity = int(request.POST.get('quantity'))
        price = int(request.POST.get('price'))
        serialnumber= request.POST.get('serialnumber')
        branch= request.POST.get('branch')
        try:
            product = new.objects.get(id=product_id)
        except new.DoesNotExist:
            return HttpResponse('تأكد من كتابة ال ID بشكل صحيح')

        if int(quantity) <= 0:
            return HttpResponse('اكتب الكمية بشكل صحيح')
        
        if int(quantity) > product.Quantity:
            return HttpResponse('الكمية المتاحة في المخزن غير كافية')
        
        # create new invoice
        
        new_invoice = invoice_new(Name= customer_name, Phone=customer_phone, Price=price, Ram= ram, HardDisk= hard, HardDisk_Other= hard2, SN= serialnumber, Branch= branch)
        new_invoice.save()
        new_invoice.Product_id.add(product)
        new_invoice.Quantity = quantity
        new_invoice.save()
        product.Quantity -= quantity
        product.save()
        return HttpResponseRedirect(f'/management/invoicesfromstock/newinvoice/newinvoiceview/{new_invoice.id}') # ده اللينك اللي هيبعتني ليه
    else:
        products = new.objects.all()  # Retrieve all products from the database
        context = {'newlaptop': products}
        return render(request, 'management/newlaptopfromstock.html', context)  # هنا اسم الصفحه اللي هيعرض عليها

@login_required
def new_invoice_view(request, invoice_id):
    if not request.user.is_staff:
        return render(request, 'management/error.html')
    invoice_obj = invoice_new.objects.get(id=invoice_id)
    product = invoice_obj.Product_id.first()
    context = {'invoice_obj': invoice_obj, 'product': product}
    Totalprice= invoice_obj.Price * invoice_obj.Quantity
    context['Totalprice'] = Totalprice
    if invoice_obj.Branch == "computer_souq":
        return render(request, 'management/computersouqnewinvoice.html', context)
    elif invoice_obj.Branch == 'carnival':
        return render(request, 'management/carnivalnewinvoice.html', context)
    elif invoice_obj.Branch == 'sajed':
        return render(request, 'management/sajednewinvoice.html', context)
    elif invoice_obj.Branch == 'carnival_plus':
        return render(request, 'management/carnival_plusnewinvoice.html', context)
    else:
        return HttpResponse('Error505')
#######################################################################################################################################
### فواتير الاستعمال ###
@login_required
def used_invoice(request):
    if not request.user.is_staff:
        return render(request, 'management/error.html')
    if request.method == 'POST': # البوست المرفوع من ال FORM 
        product_id = request.POST.get('product_id')
        customer_name = request.POST.get('customer_name')
        customer_phone = request.POST.get('customer_phone')
        ram = request.POST.get('ram')
        hard = request.POST.get('hard')
        hard2=request.POST.get('hard2')
        quantity = int(request.POST.get('quantity'))
        price = int(request.POST.get('price'))
        serialnumber= request.POST.get('serialnumber')
        branch= request.POST.get('branch')
        try:
            product = used.objects.get(id=product_id)
        except used.DoesNotExist:
            return HttpResponse('تأكد من كتابة ال ID بشكل صحيح')

        if int(quantity) <= 0:
            return HttpResponse('اكتب الكمية بشكل صحيح')
        
        if int(quantity) > product.Quantity: 
            return HttpResponse('الكمية المتاحة في المخزن غير كافية')
        
        # create new invoice
        
        used_invoice = invoice_used(Name= customer_name, Phone=customer_phone, Price=price, Ram= ram, HardDisk= hard, HardDisk_Other= hard2, SN= serialnumber, Branch= branch)
        used_invoice.save()
        used_invoice.Product_id.add(product)
        used_invoice.Quantity = quantity
        used_invoice.save()
        product.Quantity -= quantity
        product.save()
        return HttpResponseRedirect(f'/management/invoicesfromstock/usedinvoice/usedinvoiceview/{used_invoice.id}') # ده اللينك اللي هيبعتني ليه
    else:
        products = used.objects.all()  # Retrieve all products from the database
        context = {'usedlaptop': products}
        return render(request, 'management/usedlaptopfromstock.html', context) 

@login_required
def used_invoice_view(request, invoice_id):
    if not request.user.is_staff:
        return render(request, 'management/error.html')
    invoice_obj = invoice_used.objects.get(id=invoice_id)
    product = invoice_obj.Product_id.first()
    context = {'invoice_obj': invoice_obj, 'product': product}
    Totalprice= invoice_obj.Price * invoice_obj.Quantity
    context['Totalprice'] = Totalprice
    if invoice_obj.Branch == "computer_souq":
        return render(request, 'management/computersouqusedinvoice.html', context)
    elif invoice_obj.Branch == 'carnival':
        return render(request, 'management/carnivalusedinvoice.html', context)
    elif invoice_obj.Branch == 'sajed':
        return render(request, 'management/sajedusedinvoice.html', context)
    elif invoice_obj.Branch == 'carnival_plus':
        return render(request, 'management/carnival_plususedinvoice.html', context)
    else:
        return HttpResponse('Error404')
#######################################################################################################################################
### Sheets ###
@login_required
def rams(request):
    if not request.user.is_staff:
        return render(request, 'management/error.html')
    rams = ram.objects.all()
    context = {'rams': rams}
    return render(request, 'management/ramssheet.html', context)
@login_required
def newlaptopsstock(request):
    if not request.user.is_staff:
        return render(request, 'management/error.html')
    newlaptops = new.objects.all()
    context = {'newlaptops': newlaptops}
    return render(request, 'management/newlaptopssheet.html', context)
@login_required
def usedlaptopsstock(request):
    if not request.user.is_staff:
        return render(request, 'management/error.html')
    usedlaptops = used.objects.all()
    context = {'usedlaptops': usedlaptops}
    return render(request, 'management/usedlaptopssheet.html', context)
@login_required
def hardsstock(request):
    if not request.user.is_staff:
        return render(request, 'management/error.html')
    hardsstock = hard.objects.all()
    context = {'hardsstock': hardsstock}
    return render(request, 'management/harddisksheet.html', context)
#######################################################################################################################################
### Out of Stock ###
#######################################################################################################################################
### Add Products ###
@login_required
def addproducts(request):
    if not request.user.is_staff:
        return render(request, 'management/error.html')
    return render(request, 'management/addproducts.html')