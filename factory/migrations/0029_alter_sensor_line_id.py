# Generated by Django 3.2.6 on 2021-11-04 08:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('factory', '0028_sensor_line_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensor',
            name='line_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='factory.productline'),
        ),
    ]
