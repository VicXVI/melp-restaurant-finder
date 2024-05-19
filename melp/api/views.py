from rest_framework import generics, status
from .models import Restaurants
from .serializers import RestaurantSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from geopy.distance import distance
from statistics import mean
from statistics import stdev

class RestauranteBaseView(generics.GenericAPIView):
    queryset = Restaurants.objects.all()
    serializer_class = RestaurantSerializer
#Create Restaurant view
class RestaurantCreateView(RestauranteBaseView, generics.CreateAPIView):
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        response_data = {
            "msg": "Successfully created a restaurant",
            "data": response.data
        }
        return Response(response_data, status=status.HTTP_201_CREATED)

#Retrieve Restaurant view
class RestaurantReadView(RestauranteBaseView, generics.RetrieveAPIView):
    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        response_data = {
            "msg": "Successfully retrieved restaurant data",
            "data": response.data,
        }
        return Response(response_data, status=status.HTTP_200_OK)

#Update Restaurant view
class RestaurantUpdateView(RestauranteBaseView, generics.UpdateAPIView):
    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        response_data = {
            "msg": "Successfully updated restaurant data",
            "data": response.data
        }
        return Response(response_data, status=status.HTTP_200_OK)

#Delete Restaurant view
class RestauranteDestroyView(RestauranteBaseView, generics.DestroyAPIView):
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        response_data = {
            "message": "Successfully deleted restaurant"
        }
        return Response(response_data, status=status.HTTP_204_NO_CONTENT)
    
class RestauranteListView(generics.ListAPIView):
    queryset = Restaurants.objects.all()
    serializer_class = RestaurantSerializer
    
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