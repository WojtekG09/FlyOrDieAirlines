import datetime

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models

class Airport(models.Model):
    airport_code = models.CharField(max_length=3, primary_key=True)
    airport_name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=30)

    def __str__(self):
        return self.airport_name


class Airline(models.Model):
    airline_code = models.CharField(max_length=3, primary_key=True)
    airline_name = models.CharField(max_length=100)


class Aircraft(models.Model):
    aircraft_code = models.CharField(max_length=3, primary_key=True)
    aircraft_type = models.CharField(max_length=100)
    max_capacity = models.IntegerField()

    def __str__(self):
        return self.aircraft_code + " " +  self.aircraft_code



class Flight(models.Model):
    flight_id = models.AutoField(primary_key=True)
    airline_code = models.ForeignKey(Airline, on_delete=models.CASCADE)
    departure_airport_code = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='departure_airport')
    arrival_airport_code = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='arrival_airport')
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    aircraft_code = models.ForeignKey(Aircraft, on_delete=models.CASCADE)

    def clean(self):
        if self.departure_time > self.arrival_time:
            raise ValidationError('departure date cannot be later than arrival date.')
        if self.departure_airport_code == self.arrival_airport_code:
            raise ValidationError('departure airport cannot be same as the arrival airport.')


class Reservation(models.Model):
    reservation_id = models.AutoField(primary_key=True)
    flight_id = models.ForeignKey(Flight, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=10)
    date_reserved = models.DateField()
