from django.db import models

# Create your models here.todocarform-float: left; margin-right: 1rem; 


class MoreInfo(models.Model):
    TYPE = {
        (0, 'Other'),
        (1, 'Sedan'),
        (2, 'Wagon'),
        (3, 'Truck'),
        (4, 'Compact'),
        (5, 'Coupe'),
    }
    maximum_speed = models.PositiveSmallIntegerField(default=0)
    body_type = models.PositiveSmallIntegerField(default=0, choices=TYPE)


class Vehicle(models.Model):
    car_brand = models.CharField(max_length=30, blank=False)
    car_model = models.CharField(max_length=20, default='unknown')
    car_specification = models.TextField(default=" no description ")
    production_from = models.DateField(null=True, blank=True)
    production_to = models.DateField(null=True, blank=True)
    acceleration_0_to_100 = models.DecimalField(
        max_digits=4, decimal_places=1, null=True, blank=True)
    illustrative_photo = models.ImageField(
        upload_to="carimages", null=True, blank=True)
    additional = models.OneToOneField(
        MoreInfo, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.brand_with_model()

    def brand_with_model(self):
        return "{} {}".format(self.car_brand, self.car_model)


class Rating(models.Model):
    opinion = models.TextField(default="", blank=True)
    coolness_rating = models.PositiveSmallIntegerField(default=5)
    car = models.ForeignKey(Vehicle, on_delete=models.CASCADE)


class Fuel(models.Model):
    fuel_designation = models.CharField(max_length=23)
    cars = models.ManyToManyField(Vehicle)
