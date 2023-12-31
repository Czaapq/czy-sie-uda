# Generated by Django 4.2.7 on 2023-11-29 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carweb', '0005_vehicle_production_from_vehicle_production_to'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='acceleration_0_to_100',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='illustrative_photo',
            field=models.ImageField(blank=True, null=True, upload_to='carimages'),
        ),
    ]
