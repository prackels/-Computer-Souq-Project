from .models import *
from rest_framework import serializers
class UsedSerializers(serializers.ModelSerializer):
    class Meta:
        model= used
        fields= '__all__'

class NewSerializers(serializers.ModelSerializer):
    class Meta:
        model= new
        fields= '__all__'
class RamSerializers(serializers.ModelSerializer):
    class Meta:
        model= ram
        fields= '__all__'
class HardSerialzers(serializers.ModelSerializer):
    class Meta:
        model= hard
        fields= '__all__'
class RamSerializers(serializers.ModelSerializer):
    class Meta:
        model= ram
        fields= '__all__'
class BagSerializers(serializers.ModelSerializer):
    class Meta:
        model= bag
        fields= '__all__'
