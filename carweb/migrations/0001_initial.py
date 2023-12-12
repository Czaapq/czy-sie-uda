# Generated by Django 4.2.7 on 2023-12-12 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MoreInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maximum_speed', models.PositiveSmallIntegerField(default=0)),
                ('body_type', models.PositiveSmallIntegerField(choices=[(2, 'Wagon'), (5, 'Coupe'), (3, 'Truck'), (1, 'Sedan'), (4, 'Compact'), (0, 'Other')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_brand', models.CharField(max_length=30)),
                ('car_model', models.CharField(default='unknown', max_length=20)),
                ('car_specification', models.TextField(default=' no description ')),
                ('production_from', models.DateField(blank=True, null=True)),
                ('production_to', models.DateField(blank=True, null=True)),
                ('acceleration_0_to_100', models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True)),
                ('illustrative_photo', models.ImageField(blank=True, null=True, upload_to='carimages')),
                ('additional', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='carweb.moreinfo')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opinion', models.TextField(blank=True, default='')),
                ('coolness_rating', models.PositiveSmallIntegerField(default=5)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carweb.vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='Fuel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fuel_designation', models.CharField(max_length=23)),
                ('cars', models.ManyToManyField(to='carweb.vehicle')),
            ],
        ),
    ]
