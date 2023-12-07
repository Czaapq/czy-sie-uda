
from django.urls import path
from carweb.views import all_cars, new_car, edit_car, delete_car
urlpatterns = [

    path('all/', all_cars, name="all_cars"),
    path('new/', new_car, name="new_car"),
    path('edit/<int:id>/', edit_car, name="edit_car"),
    path('delete/<int:id>/', delete_car, name = "delete_car")
]
