from django.db import models

# Create your models here.
class Flight(models.Model):
    flight_number = models.CharField(max_length=20)
    airline = models.CharField(max_length=100)
    departure_airport = models.CharField(max_length=3)
    departure_city = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    arrival_airport = models.CharField(max_length=3)
    arrival_city = models.CharField(max_length=100)
    arrival_time = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available_seats = models.IntegerField()