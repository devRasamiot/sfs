from django.contrib import admin
from .models import Factory, Shift,ShopFloor, ProductLine, ProductSubLine, SensorType, Sensor

# Register your models here.
admin.site.register(Factory)
admin.site.register(Shift)
admin.site.register(ShopFloor)
admin.site.register(ProductLine)
admin.site.register(ProductSubLine)
admin.site.register(SensorType)
admin.site.register(Sensor)