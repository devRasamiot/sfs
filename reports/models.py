from typing import Callable
from django.db import models
from django.db.models.fields.related import ForeignKey
from django.db.models.deletion import CASCADE, SET_NULL
from factory.models import Factory, Sensor, Shift
# Create your models here.



# class LiveReports(models.Model):
#     shift_time = ForeignKey(Shift, on_delete=CASCADE)
#     sensor = ForeignKey(Sensor, on_delete=CASCADE)
#     dataAggregated = models.FloatField(default=0)

#     def __str__(self) :
#         return f'{self.name}'
