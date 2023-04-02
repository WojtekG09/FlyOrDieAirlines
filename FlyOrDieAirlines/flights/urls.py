from django.urls import path
from . import views
from django.contrib.auth import views as auth_view


app_name = "flights"

urlpatterns = [
  #  path("", views.homepage, name="homepage"),
    path("", views.home, name = 'home' ),
    path('login/', auth_view.LoginView.as_view(template_name='flights/login.html'), name="login"),
    path("register.html", views.register_page)
]