from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from flights.models import Flight
# Create your views here.
@api_view(['GET'])
def firstRoute(request) :
    message = f'Wellcome to home'
    
    return Response(message)

@api_view(['POST'])
def flightsFilter(request) :
    if request.method == 'POST':
        # Retrieve form data
        departure_city = request.POST.get('departure_city')
        arrival_city = request.POST.get('arrival_city')
        trip_type = request.POST.get('trip_type')
        min_price = request.POST.get('min_price')
        max_price = request.POST.get('max_price')
        
        # Filter flights based on criteria
        flights = Flight.objects.filter(
            departure_city__iexact=departure_city,
            arrival_city__iexact=arrival_city,
            price__gte=min_price,
            price__lte=max_price
        )
        if trip_type == 'oneWay':
            # Perform one-way flight search
            search_results = flights
        
        elif trip_type == 'roundTrip':
            # For round trip, also filter return flights
            return_flights = Flight.objects.filter(
                departure_city__iexact=arrival_city,
                arrival_city__iexact=departure_city,
                price__gte=min_price,
                price__lte=max_price
            )
            
            search_results = {'outbound': flights, 'return': return_flights}
    
    return Response(search_results)