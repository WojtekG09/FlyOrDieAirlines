from django.urls import path
from . import views
from django.contrib.auth import views as auth_view
from django.contrib.auth import views as auth_views

app_name = "flights"

urlpatterns = [
    path("", views.home, name = 'home' ),
    path("login/", views.login_page, name="login"),
    path("register/", views.register_page, name="register"),
    path("search/", views.search, name="search"),
    path('logout/', views.logout_view, name='logout'),

]