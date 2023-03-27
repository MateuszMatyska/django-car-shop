from .. import models
from .. import helpers

def get_cars():
    return models.Car.objects.all()

def get_car(car_id):
    return models.Car.objects.get(id=car_id)

def search_cars(searching_input):
    searching_results = ''
    if type(searching_input) is str:
        cars_by_brand = models.Car.objects.filter(brand_name = str(searching_input))
        cars_by_model = models.Car.objects.filter(model_name = str(searching_input))
        searching_results = cars_by_brand | cars_by_model 
    
    if helpers.is_argument_int(searching_input) == True:
        cars_by_year = models.Car.objects.filter(year = int(searching_input))
        searching_results = cars_by_year 
    
    if helpers.is_argument_float(searching_input) == True and helpers.is_argument_int(searching_input) == False:
        cars_by_engine = models.Car.objects.filter(engine = int(searching_input))
        cars_by_price = models.Car.objects.filter(price = int(searching_input))
        searching_results = cars_by_engine | cars_by_price

    return searching_results