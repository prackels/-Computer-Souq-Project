from django.shortcuts import render
from products.models import *

def home(request):
    useds = used.objects.filter(Active = True, Active_Home=True, Quantity__gte=1 )[:4]
    news = new.objects.filter(Active= True, Active_Home=True, Quantity__gte=1)[:4]
    context = {'used': useds, 'new': news}
    return render(request, 'main/home.html', context)
def about(request):
    return render(request, 'main/about.html')
def services(request):
    return render(request, 'main/services.html')