from django.urls import path
from .views import RestaurantList, RestaurantDetail
from . import views

urlpatterns = [
    path("restaurants/", RestaurantList.as_view()),
    path("restaurants/<str:pk>/", RestaurantDetail.as_view()),
    path('restaurants/statistics',views.statistics),
]