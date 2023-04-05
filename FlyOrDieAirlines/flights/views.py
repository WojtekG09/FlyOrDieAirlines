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



def search(request):
    products = Airport.objects.all()
    return render(request, 'product_list.html', {'products': products})

def logout_view(request):
    logout(request)
    return render(request, 'flights/logout.html')