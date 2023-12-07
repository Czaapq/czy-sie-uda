from django.forms import ModelForm
from .models import Vehicle, MoreInfo, Rating


class VehicleForm(ModelForm):
    class Meta:
        model = Vehicle
        fields = ['car_brand', 'car_model', 'car_specification', 'production_from',
                  'production_to', 'acceleration_0_to_100', 'illustrative_photo']


form = VehicleForm()


class MoreInfoForm(ModelForm):
    class Meta:
        model = MoreInfo
        fields = ['maximum_speed', 'body_type']




class RatingForm(ModelForm):
    class Meta:
        model = Rating
        fields = ['coolness_rating', 'opinion']

