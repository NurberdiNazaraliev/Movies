from django.contrib import admin
from django.urls import path, include
from .views import *

router = DefaultRouter()
router.register(r'adminMoviesView', adminMoviesView)


urlpatterns = [
    path('api/drf-auth', include('rest_framework.urls')),
    path('movies/', MoviesView.as_view(), name="movies"),
    path('', include(router.urls)),
    path('reviews/', ReviewsView.as_view(), name="reviews"),
    path("reviewpost/", ReviewCreateAPIView.as_view(), name="review-create"),
    path('purchaces/',UserPurchaseHistoryView.as_view(), name="purchase-history")
]