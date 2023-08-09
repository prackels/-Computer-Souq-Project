from django.shortcuts import render
from .models import *
from django.views.generic import DetailView
from rest_framework import viewsets, filters
from .serializers import *

class used_detailes(DetailView):
    model = used
    template_name = 'products/useddetailes.html'
    context_object_name = 'useddetailes'
    
class new_detailes(DetailView):
    model = new
    template_name = 'products/newdetailes.html'
    context_object_name = 'newdeatiles'
    
    

def products(request):
    return render(request, 'products/products.html')
def useds(request):
    return render(request, 'products/used.html')
def news(request):
    return render(request, 'products/new.html')

class usedapi(viewsets.ModelViewSet):
    queryset = used.objects.all()
    serializer_class = UsedSerializers 
    search_fields = ['id']
    filter_backends = [filters.SearchFilter]

    
