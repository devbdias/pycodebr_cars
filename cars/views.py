from django.shortcuts import render, redirect
from .models import Car
from .forms import CarForm

def cars_view(request):
    cars = Car.objects.all().order_by('brand__name')
    search = request.GET.get('search')
    if search:
        cars = cars.filter(model__icontains=search).order_by('brand__name')
    return render(request, 'cars.html', {'cars': cars})

def new_car_view(request):
    if request.method == "POST":
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('cars_list')
    else:
        form = CarForm()
    return render(request, 'new_car.html', {'form': form})