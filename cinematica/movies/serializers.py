from rest_framework import serializers
from .models import *
from cinematheater.models import Reservation


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class MovieReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieReview
        fields = '__all__'


class UserPurchaseHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'