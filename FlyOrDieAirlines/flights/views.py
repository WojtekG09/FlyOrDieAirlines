from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Airport, Flight, Reservation
# from .forms import ReservationForm
from datetime import datetime, date
from django.db.models.functions import TruncDate

def	home(request):
    airports = Airport.objects.all()

    return render(request, 'flights/index.html', {'airports': airports})

def reservation_page(request):
	return render(request, 'flights/reservation_form.html')

def summary_page(request):
	return render(request, 'flights/summary.html')

def about_page(request):
	return render(request, 'flights/about.html')

@login_required
def profile_page(request):

    if request.method == 'POST' :
        print(request.POST)
        username = request.POST.get('username')
        print(username)
        reservations = Reservation.objects.filter(
            user=username
        )

        return render(request, 'flights/profile.html', {'reservations': reservations})
    return render(request, 'flights/profile.html')

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Username or password is incorrect')
    return render(request, 'flights/login.html', {})


def register_page(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, your account was created successfully')
            return redirect('/')
    else:
        form = UserRegisterForm()

    return render(request, 'flights/register.html', {'form': form})


def logout_view(request):
    logout(request)
    return render(request, 'flights/logout.html')

def search(request):


    if request.method == 'POST' :
        print(request.POST)
        from_city = request.POST.get('from_city')
        to_city = request.POST.get('to_city')
        departure_datetime = datetime.strptime(request.POST.get('depature1'), '%Y-%m-%d')
        departure_date = datetime.date(departure_datetime)
        print(from_city)
        print(to_city)
        print(departure_date)
        if len(request.POST) == 5:
            return_datetime = datetime.strptime(request.POST.get('depature2'), '%Y-%m-%d')
            return_date = return_datetime
            print("weszlo 5")
            flights = Flight.objects.filter(
                departure_airport_code=from_city,
                arrival_airport_code=to_city,
                departure_time__date=departure_date,
            )
            return_flights = Flight.objects.filter(
                departure_airport_code=to_city,
                arrival_airport_code=from_city,
                departure_time__date=return_date,
            )
            return render(request, 'flights/search.html', {'flights': flights, 'return_flights': return_flights})
        elif len(request.POST) == 4:
            print("weszlo 4")

            flights = Flight.objects.filter(
                departure_airport_code=from_city,
                arrival_airport_code=to_city,
                departure_time__date=departure_date,
            )
            return render(request, 'flights/search.html', {'flights': flights})

        print(len(request.POST))

    return render(request, 'flights/search.html')

@login_required
def logout_view(request):
    logout(request)
    return render(request, 'flights/logout.html')
@login_required
def delete_reservation(request, reservation_id):
    reservation = Reservation.objects.get(reservation_id=reservation_id)
    reservation.delete()
    return redirect('/profile')

# @login_required
# def make_reservation(request):
#     return
#     if request.method == 'POST':
#         form = ReservationForm(request.POST)
#         if form.is_valid():
#
#
#     else:
#         form = ReservationForm()
#     return render(request, 'reservation_form.html', {'form': form})

