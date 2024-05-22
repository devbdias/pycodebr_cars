from django.shortcuts import render
from cars.models import Car

def cars_view(request):

    cars = Car.objects.all()
    for car in cars:
        print(car.photo)
        
    return render(
        request, 
        'cars.html', 
        {'cars': cars}
    )
