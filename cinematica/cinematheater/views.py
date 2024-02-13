from django.shortcuts import render
from django.http import Http404
from django.shortcuts import render
from rest_framework import generics, views, status, permissions
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from django.urls import path, include
from rest_framework.response import Response
from rest_framework.routers import DefaultRouter
from rest_framework.views import APIView
from .models import *
from .serializers import *
from .serializers import *
from .models import *
from rest_framework.generics import ListAPIView, get_object_or_404
from django.utils import timezone
from datetime import datetime, timedelta, time

# Create your views here.
class CinemasView(ListAPIView):
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer

class adminCinemasView(viewsets.ModelViewSet):
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer
    permission_classes = [IsAdminUser]

class RoomsView(ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAdminUser]

class adminRoomsView(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAdminUser]



class ReservationView(ListAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


class ReservationCreateView(APIView):
    def post(self, request, format=None):
        serializer = ReservationSerializer(data=request.data)
        if serializer.is_valid():
            # Check if the user is authenticated
            if request.user.is_authenticated:
                # Set the user for the reservation
                serializer.save(user=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({"error": "Authentication required."}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
