from django.urls import include, path 
from . import views 
from .views import *
from rest_framework.routers import DefaultRouter # lazm a3ml import ll DefaultRouter

router = DefaultRouter()
router.register('used', views.usedapi)

urlpatterns = [
    path('', views.products, name='products'),
    path('used/', views.useds, name='used'),
    path('new/', views.news, name='new'),
    path('more/used/<int:pk>/', used_detailes.as_view(), name='useddetailes'),
    path('more/new/<int:pk>/', new_detailes.as_view(), name='newdetailes'),
    path('usedapi/', include(router.urls)),
]