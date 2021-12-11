from django.shortcuts import render
from ..models.car_model import Car

def cars_view(request):
   cars = Car.objects.all()
   return render(request,'cars_temp.html', {'cars':cars})



def filter_cars(request):
    if request.method == "POST":
        searched = request.POST['searchcar']
        cars = Car.objects.filter(car_name__icontains = searched)
        return render(request,'search_cars.html',{'searched':searched,'cars':cars})
    else:
        return render(request,'search_cars.html',{})