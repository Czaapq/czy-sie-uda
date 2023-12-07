from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Vehicle, MoreInfo, Rating
from .forms import VehicleForm, MoreInfoForm, RatingForm
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import UserSerializer, VehicleSerializer

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class VehicleView(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer



def all_cars(request):
    wholeCars = Vehicle.objects.all()

    return render(request, 'cars.html', {'cars': wholeCars})


@login_required
def new_car(request):
    form_vehicle = VehicleForm(request.POST or None, request.FILES or None)
    form_more = MoreInfoForm(request.POST or None)

    if all((form_vehicle.is_valid(), form_more.is_valid())):
        car = form_vehicle.save(commit=False)
        more = form_more.save()
        car.additional = more
        car.save()
        return redirect(all_cars)

    return render(request, 'car_form.html', {'form': form_vehicle, 'form_more': form_more, 'new': True})


@login_required
def edit_car(request, id):
    car = get_object_or_404(Vehicle, pk=id)
    ratings = Rating.objects.filter(car=car)
    try:
        more = MoreInfo.objects.get(vehicle=car.id)
    except MoreInfo.DoesNotExist:
        more = None

    form_vehicle = VehicleForm(request.POST or None,
                               request.FILES or None, instance=car)

    form_more = MoreInfoForm(request.POST or None, instance=more)

    form_rating = RatingForm(request.POST or None,)

    if request.method == 'POST':
        if 'coolness_rating' in request.POST:
            rating = form_rating.save(commit=False)
            rating.car = car
            rating.save()

    if all((form_vehicle.is_valid(), form_more.is_valid())):
        car = form_vehicle.save(commit=False)
        more = form_more.save()
        car.additional = more
        car.save()
        return redirect(all_cars)

    return render(request, 'car_form.html', {'form': form_vehicle, 'form_more': form_more, 'ratings': ratings, 'form_rating' : form_rating, 'new': False})


@login_required
def delete_car(request, id):
    car = get_object_or_404(Vehicle, pk=id)

    if request.method == "POST":
        car.delete()
        return redirect(all_cars)

    return render(request, 'confirm.html', {'car': car})
