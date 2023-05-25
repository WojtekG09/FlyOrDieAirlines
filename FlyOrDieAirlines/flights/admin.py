from django.contrib import admin
from .models import Airport, Flight, Airline, Aircraft, Reservation

# Register your models here.
admin.site.register(Airport)
admin.site.register(Flight)
admin.site.register(Airline)
admin.site.register(Aircraft)
admin.site.register(Reservation)