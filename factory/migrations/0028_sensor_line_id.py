# Generated by Django 3.2.6 on 2021-11-04 08:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('factory', '0027_auto_20211017_0929'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensor',
            name='line_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='factory.productline'),
        ),
    ]