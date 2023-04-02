from django.http import	HttpResponse
from django.shortcuts import render
from .models import Airport

# def	home(request):
# 	return render(request, 'flights/index.html')
def	home(request):
    airports = Airport.objects.all()
    return render(request, 'flights/index.html', {'airports': airports})

def login_page(request):
	return render(request, 'flights/login.html')

def register_page(request):
	return render(request, 'flights/register.html')
