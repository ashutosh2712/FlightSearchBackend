from django.urls import path
from flights import views
urlpatterns = [
    path('', views.getFlights,name="get-flights"),
    path('filterflights', views.flightsFilter,name="flights-filter"),
    
]