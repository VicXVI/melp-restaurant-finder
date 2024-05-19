from rest_framework import generics
from .models import Restaurants
from .serializers import RestaurantSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from geopy.distance import distance
from statistics import mean
from statistics import stdev

#Read and write a collection of restaurant model
class RestaurantList(generics.ListCreateAPIView):
    serializer_class = RestaurantSerializer
    def get_queryset(self):
        queryset = Restaurants.objects.all()
        return queryset
    
#Read, write and delete a single entry of restaurant model
class RestaurantDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RestaurantSerializer
    queryset = Restaurants.objects.all()

#Retrieve statistics of all the restaurants inside the radius of a given location
@api_view(('GET',))
def statistics(request):
    latitude = float(request.query_params.get('latitude'))
    longitude = float(request.query_params.get('longitude'))
    radius = float(request.query_params.get('radius'))
    current_location = (latitude, longitude)
    restaurants = Restaurants.objects.all()
    inside_radius = []
    ratings = []
    for restaurant in restaurants:
        current_restaurant = (restaurant.lat, restaurant.lng)
        print(distance(current_location, current_restaurant))
        if distance(current_location, current_restaurant) <= radius:
            inside_radius.append(restaurant)
            ratings.append(restaurant.rating)
    if len(ratings) > 1:
        std_dev = stdev(ratings)
    else:
        std_dev = 0.0
    response_data = {
        "count": len(inside_radius),
        "avg": mean(ratings),
        "std": std_dev,
    }
    return Response(response_data)