from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Airport, Flight
# from .forms import ReservationForm
from datetime import datetime
from django.db.models.functions import TruncDate

def	home(request):
    airports = Airport.objects.all()

    return render(request, 'flights/index.html', {'airports': airports})

def reservation_page(request):
	return render(request, 'flights/reservation_form.html')



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


    if request.method == 'POST':
        # print(request.POST)
        from_city = request.POST.get('from_city')
        to_city = request.POST.get('to_city')
        departure_date = request.POST.getlist('depature_date')
        arrival_date = request.POST.get('arrival_date')
        # print(request.POST.get('select_from'))
        # departure_date = datetime.strptime(str(request.GET.get('depature')), '%Y-%m-%d ')
        # arrival_date = datetime.strptime(request.GET.get('arrival'), '%Y-%m-%d ')

        print(from_city)
        print(departure_date)


        # Entry.objects.filter(pub_date__date=datetime.date(2005, 1, 1))

        # Filter flights based on search parameters
        flights = Flight.objects.filter(
             departure_airport_code=from_city,
             arrival_airport_code=to_city,
            # departure__date=departure_date,
            # arrival__date=arrival_date
        )
        for flight in flights:
            print(flight)


#             .annotate(
#             departure_date_only=TruncDate('departure_date'),
#             arrival_date_only=TruncDate('arrival_date')
# )



        # Render template with search results
        return render(request, 'flights/search.html', {'flights': flights})

    # Render the search form if no search parameters are provided
    return render(request, 'flights/search.html')

def logout_view(request):
    logout(request)
    return render(request, 'flights/logout.html')







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

