from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('search_cars/<str:searching_input>', views.search_cars, name='search_car')
]
