from django.shortcuts import render
from django.http import HttpResponse

from . import models

def index(request):
    cars = models.Car.objects.all()
    context = {'cars_list': cars}
    return render(request, 'cars/index.html', context)

