# from functools import _Descriptor
from typing import Callable
from django.db import models
from django.db.models.base import Model
# from django.contrib.auth.models import User
from django.conf import settings
from PIL import Image
from django.db.models.deletion import CASCADE, SET_NULL
from django.db.models.query_utils import select_related_descend

User = settings.AUTH_USER_MODEL

# Create your models here.
class Factory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    owner = models.ManyToManyField(User, related_name='factories')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class Shift(models.Model):
    name = models.CharField(max_length=100)
    start_time = models.TimeField()
    end_time = models.TimeField() 
    factory_id = models.ForeignKey(Factory, on_delete=CASCADE)

    def __str__(self) :
        return f'{self.name}'


class ShopFloor(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    factory_id = models.ForeignKey(Factory, on_delete= models.CASCADE)

    def __str__(self):
        return f'{self.name}, {self.factory_id}'



class ProductLine(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    floor_id = models.ForeignKey(ShopFloor, on_delete= models.CASCADE)
    factory_id = models.ForeignKey(Factory, on_delete=CASCADE)
    
    def __str__(self):
        return f'{self.name}, {self.floor_id }'

class ProductSubLine(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    line_id = models.ForeignKey(ProductLine, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.name}, {self.line_id}'


class SensorType(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(default='default.jpg',  upload_to='sensor_pics')

    def __str__(self):
        return self.name

        
class Sensor(models.Model):
    name = models.CharField(max_length=100)
    # type = models.CharField(max_length=100)
    mac_addr = models.CharField(max_length=100)
    port = models.CharField(max_length=100)
    place_inline = models.IntegerField()
    type = models.ForeignKey(SensorType, null=True, on_delete=SET_NULL)
    updated_at = models.DateTimeField(auto_now_add=True) 

    subline_id = models.ForeignKey(ProductSubLine, on_delete=CASCADE)
    line_id = models.ForeignKey(ProductLine, on_delete=CASCADE)
    
    def __str__(self) :
        return f'{self.name}'

    