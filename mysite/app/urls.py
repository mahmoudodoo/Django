from django.urls import path
from .views.base_view import base_view
from .views.cars_view import cars_view,filter_cars

urlpatterns = [

 path('', base_view, name="base_view"),
  path('cars_view', cars_view, name="cars_view"),
  path('filter_cars',filter_cars,name="filter_cars"),

]
  