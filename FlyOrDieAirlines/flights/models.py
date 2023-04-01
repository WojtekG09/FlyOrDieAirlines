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
    website_url = models.URLField()

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

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=12)
    street_address = models.CharField(max_length=70)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    country = models.CharField(max_length=50)



class Worker(models.Model):
    worker_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    job_title = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    hire_date = models.DateField()

class Reservation(models.Model):
    reservation_id = models.AutoField(primary_key=True)
    flight_id = models.ForeignKey(Flight, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    worker_id = models.ForeignKey(Worker, on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=10)
    date_reserved = models.DateField()
    checked_in = models.BooleanField(default=False)
    baggage_count = models.IntegerField()
    baggage_weight = models.DecimalField(max_digits=10, decimal_places=2)

class ReservationHistory(models.Model):
    reservation_id = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    date_of_travel = models.DateField()
    flight_number = models.CharField(max_length=10)
    departure_airport_code = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='departure_airport_history')
    arrival_airport_code = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='arrival_airport_history')
    reservation_date = models.DateField()