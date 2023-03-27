from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('car/id=<int:car_id>',views.car_info, name='car_info'),
    path('search_cars/<str:searching_input>', views.search_cars, name='search_car')
]
