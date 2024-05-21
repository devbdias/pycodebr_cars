from django.shortcuts import render
from django.http import HttpResponse

def cars_view(request):
    return HttpResponse("Meus carros!")