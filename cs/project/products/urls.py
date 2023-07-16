from django.urls import path 
from . import views 
from .views import *
urlpatterns = [
    path('', views.products, name='products'),
    path('used/', views.useds, name='used'),
    path('new/', views.news, name='new'),
    path('more/used/<int:pk>/', used_detailes.as_view(), name='useddetailes'),
    path('more/new/<int:pk>/', new_detailes.as_view(), name='newdetailes'),
]