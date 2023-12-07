from django.contrib import admin
from .models import Vehicle, MoreInfo, Rating, Fuel
# Register your models here.

# admin.site.register(Vehicle)


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    # fields = ["car_brand"] #tutaj kontrola nad rzeczemmi jakie sie wyświetlają
    # exclude = ["description"] to wykluczamy czeo nie chcemy widziedz
    list_display = ["car_brand", "car_model", "acceleration_0_to_100"]
    list_filter = ["car_brand",]
    search_fields = ["car_brand"]


admin.site.register(MoreInfo)
admin.site.register(Rating)
admin.site.register(Fuel)