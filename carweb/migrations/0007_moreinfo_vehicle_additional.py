# Generated by Django 4.2.7 on 2023-12-05 16:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carweb', '0006_vehicle_acceleration_0_to_100_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MoreInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maximum_speed', models.PositiveSmallIntegerField(default=0)),
                ('body_type', models.PositiveSmallIntegerField(choices=[(2, 'Wagon'), (1, 'Sedan'), (4, 'Compact'), (3, 'Truck'), (0, 'Other'), (5, 'Coupe')], default=0)),
            ],
        ),
        migrations.AddField(
            model_name='vehicle',
            name='additional',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='carweb.moreinfo'),
        ),
    ]