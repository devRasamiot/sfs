# Generated by Django 3.2.6 on 2021-10-17 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('factory', '0025_alter_shift_end_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shift',
            name='start_time',
            field=models.TimeField(),
        ),
    ]
