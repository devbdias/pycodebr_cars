from django.shortcuts import render
from cars.models import Car

def cars_view(request):
    cars = Car.objects.all().order_by('brand__name')

    search = request.GET.get('search')

    if search:
        cars = cars.filter(model__icontains=search).order_by('brand__name')
        
    return render(request, 'cars.html', {'cars': cars})
