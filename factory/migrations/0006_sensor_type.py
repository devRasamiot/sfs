# Generated by Django 3.2.6 on 2021-09-02 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('factory', '0005_rename_production_line_product_line'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('icon', models.ImageField(default='default.jpg', upload_to='')),
            ],
        ),
    ]