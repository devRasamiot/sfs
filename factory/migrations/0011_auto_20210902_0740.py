# Generated by Django 3.2.6 on 2021-09-02 07:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('factory', '0010_sensor'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Product_line',
            new_name='ProductLine',
        ),
        migrations.RenameModel(
            old_name='Sensor_type',
            new_name='SensorType',
        ),
        migrations.RenameModel(
            old_name='Shop_floor',
            new_name='ShopFloor',
        ),
    ]
