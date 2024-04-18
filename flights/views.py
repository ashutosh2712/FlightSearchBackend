from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from flights.models import Flight
from flights.serializers import FlightSerializer
# Create your views here.
@api_view(['GET'])
def getFlights(request) :
    flights = Flight.objects.all()
    
    serializer = FlightSerializer(flights,many=True)
    
    return Response(serializer.data)

@api_view(['POST'])
def flightsFilter(request) :
    # Retrieve form data
    data = request.data
    departure_city = data['departure_city']
    arrival_city = data['arrival_city']
    trip_type = data['trip_type']
    min_price = data['min_price']
    max_price = data['max_price']
    
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
        
    serializer = FlightSerializer(search_results,many=True)
    
    
    return Response(serializer.data)