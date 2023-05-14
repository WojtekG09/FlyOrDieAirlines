
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Reservation, Airport


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ReservationFrom(forms.ModelForm):
    class Meta:
        model = Airport
        fields = ['country', 'city']
    widgets = {
        'city': forms.TextInput(attrs={'placeholder': 'From'}),
    }
