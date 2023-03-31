from django.contrib import admin
from .models import Airport, Flight, Airline, Aircraft, Worker, Reservation, ReservationHistory, User



# Register your models here.
admin.site.register(Airport)
admin.site.register(Flight)
admin.site.register(Airline)
admin.site.register(Aircraft)