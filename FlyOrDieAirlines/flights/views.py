from django.http import	HttpResponse
from django.shortcuts import render


def	home(request):
	return render(request, 'flights/index.html')

def login_page(request):
	return render(request, 'flights/login.html')
