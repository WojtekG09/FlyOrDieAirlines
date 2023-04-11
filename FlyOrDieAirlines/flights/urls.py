from django.urls import path
from . import views
from django.contrib.auth import views as auth_view
from django.contrib.auth import views as auth_views

app_name = "flights"

urlpatterns = [
    path("", views.home, name = 'home' ),
    path("login/", views.login_page, name="login"),
    path("register/", views.register_page, name="register"),
    path("reservation_form/", views.reservation_page, name="reservation_form"),
    path('logout/', views.logout_view, name='logout'),
    path("search/", views.search, name="search"),
    path("summary/", views.search, name="summary"),

]