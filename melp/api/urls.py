from django.urls import path
from .views import RestauranteListView, RestaurantCreateView, RestaurantReadView, RestaurantUpdateView, RestauranteDestroyView
from . import views

urlpatterns = [
    path("restaurants/", RestauranteListView.as_view()),
    path("restaurants/create/", RestaurantCreateView.as_view()),
    path("restaurants/<str:pk>/", RestaurantReadView.as_view()),
    path("restaurants/<str:pk>/update/", RestaurantUpdateView.as_view()),
    path("restaurants/<str:pk>/delete/", RestauranteDestroyView.as_view()),
    path('restaurants/statistics',views.statistics),
]