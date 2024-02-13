from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *

cinemasrouter = DefaultRouter()
cinemasrouter.register(r'adminCinemasView', adminCinemasView)

roomsrouter = DefaultRouter()
roomsrouter.register(r'adminRoomsView', adminRoomsView)


urlpatterns = [
    path('cinemas/', CinemasView.as_view(), name="cinemas"),
    path('', include(cinemasrouter.urls)),
    path('rooms/', RoomsView.as_view(), name="rooms"),
    path('', include(roomsrouter.urls)),
    path('reservations/', ReservationView.as_view(), name="reservations"),
    path('createreservation/', ReservationCreateView.as_view(), name="createreservation")

]