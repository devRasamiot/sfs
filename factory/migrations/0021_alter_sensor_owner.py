# Generated by Django 3.2.6 on 2021-10-09 10:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('factory', '0020_productsubline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensor',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='factory.productsubline'),
        ),
    ]
