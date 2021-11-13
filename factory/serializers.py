from django.db.models import fields
from rest_framework import serializers
from .models import Factory, ProductSubLine, Sensor, ShopFloor, ProductLine, SensorType



class FactorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Factory
        # fields = ['id', 'title', 'author', 'email']
        fields = '__all__'
   
   

class ShopfloorSerializer (serializers.ModelSerializer):
    class Meta:
        model = ShopFloor
        fields = '__all__'



class ProductLineSerializer (serializers.ModelSerializer):
    class Meta:
        model = ProductLine
        fields = '__all__'

class ProductSubLineSerializer (serializers.ModelSerializer):
    class Meta:
        model = ProductSubLine
        fields = '__all__'

class SensorTypeSerializer (serializers.ModelSerializer):
    class Meta:
        model = SensorType
        fields = '__all__'

class SensorSerializer (serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = '__all__'
