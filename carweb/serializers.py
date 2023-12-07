from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Vehicle


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class VehicleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['id','car_brand', 'car_model', 'car_specification','acceleration_0_to_100']
