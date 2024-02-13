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
from .models import Movie
from .serializers import MovieSerializer
from .serializers import *
from .models import *
from rest_framework.generics import ListAPIView, get_object_or_404
from django.utils import timezone
from datetime import datetime, timedelta, time
from cinematheater.models import Reservation
# Create your views here.




class MoviesView(ListAPIView):
    ##filter the movies that are currently running for viewers
    def get_queryset(self):
        current_time = datetime.now().date()
        return Movie.objects.filter(release_date__lte=current_time,end_date__gte=current_time)

    serializer_class = MovieSerializer


class adminMoviesView(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAdminUser]

class ReviewsView(ListAPIView):
    queryset = MovieReview.objects.all()
    serializer_class = MovieReviewSerializer

class ReviewCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = MovieReview(data=request.data)
        if serializer.is_valid():
            # Check if the user has already reviewed the movie
            user = request.user
            movie_id = serializer.validated_data['movie'].id
            if MovieReview.objects.filter(user=user, movie_id=movie_id).exists():
                return Response({"error": "You've already reviewed this movie."}, status=status.HTTP_400_BAD_REQUEST)
            # Save the review
            serializer.save(user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UserPurchaseHistoryView(ListAPIView):
    serializer_class = UserPurchaseHistorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Reservation.objects.filter(user=user)