from django.shortcuts import render
from django.http import HttpResponse

from . import models
from . import helpers
from .services import car_services

def index(request):
    cars = car_services.get_cars()
    context = {'cars_list': cars}
    return render(request, 'cars/index.html', context)

def car_info(request, car_id):
    car = car_services.get_car(car_id)
    context = {'car': car}
    return render(request, 'cars/car_info.html', context)

def search_cars(request, searching_input):
    searching_results = ''

    if "<" not in searching_input: 
        searching_results = car_services.search_cars(searching_input)

    context = {'cars_list': searching_results}
    return render(request, 'cars/index.html', context) 
