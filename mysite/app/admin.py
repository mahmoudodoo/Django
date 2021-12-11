from django.contrib import admin

# Register your models here.
from .models.car_model import Car
admin.site.register(Car)
