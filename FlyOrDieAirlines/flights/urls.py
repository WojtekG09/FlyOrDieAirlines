from django.urls import path
from . import views


app_name = "flights"

urlpatterns = [
  #  path("", views.homepage, name="homepage"),
    path("", views.home, name = 'home' ),
    path("login.html", views.login_page)
]