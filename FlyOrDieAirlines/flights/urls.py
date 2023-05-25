from django.urls import path
from . import views

app_name = "flights"

urlpatterns = [
    path("", views.home, name = 'home' ),
    path("login/", views.login_page, name="login"),
    path("register/", views.register_page, name="register"),
    path("make_reservation/", views.make_reservation, name="make_reservation"),
    path("reservation_form/", views.reservation_form, name="reservation_form"),
    path('logout/', views.logout_view, name='logout'),
    path("search/", views.search, name="search"),
    path("summary/", views.summary_page, name="summary"),
    path("about/", views.about_page, name="about"),
    path("profile/", views.profile_page, name="profile"),
    path('reservation/delete/<int:reservation_id>/', views.delete_reservation, name='deleteReservation'),

]




