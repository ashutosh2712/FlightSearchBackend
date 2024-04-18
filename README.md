# Flight Search Feature

This Django project implements a flight search feature that allows users to search for flights based on various criteria such as departure city, arrival city, trip type, and price range.

## Installation

1. Clone the repository:

   git clone https://github.com/your-username/your-repository.git

3. Install dependencies using Pipenv:
   pipenv install
4. Activate the virtual environment:
   pipenv shell
5. Apply migrations:
   python manage.py migrate


API Endpoint
Endpoint: /flights/filterflights
Method: POST
Request Body: JSON object containing the following fields:
departure_city: Departure city of the flight
arrival_city: Arrival city of the flight
trip_type: Trip type (oneWay or roundTrip)
min_price: Minimum price of the flight
max_price: Maximum price of the flight

Example Request Body:

{
  "departure_city": "New York",
  "arrival_city": "Los Angeles",
  "trip_type": "oneWay",
  "min_price": 100,
  "max_price": 500
}

Response: JSON object containing the search results:

{
  "search_results": [
    {
      "flight_number": "ABC123",
      "airline": "Airline A",
      "departure_city": "New York",
      "arrival_city": "Los Angeles",
      "departure_time": "2024-04-16T08:00:00Z",
      "arrival_time": "2024-04-16T10:00:00Z",
      "price": 200.50,
      "available_seats": 100
    },
    {
      "flight_number": "XYZ789",
      "airline": "Airline B",
      "departure_city": "New York",
      "arrival_city": "Los Angeles",
      "departure_time": "2024-04-17T09:00:00Z",
      "arrival_time": "2024-04-17T12:00:00Z",
      "price": 150.75,
      "available_seats": 80
    }
  ]
}
