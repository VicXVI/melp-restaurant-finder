from rest_framework import generics
from .models import Restaurants
from .serializers import RestaurantSerializer

# Create your views here.

class RestaurantList(generics.ListCreateAPIView):
    serializer_class = RestaurantSerializer
    def get_queryset(self):
        queryset = Restaurants.objects.all()
        return queryset

class RestaurantDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RestaurantSerializer
    queryset = Restaurants.objects.all()

