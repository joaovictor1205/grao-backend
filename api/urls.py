from django.urls import path
from .views import *


urlpatterns = [
    path('register', UserRegister.as_view(), name='register'),
	path('login', UserLogin.as_view()),
	path('logout', UserLogout.as_view(),),
    path('restaurants/', RestaurantList.as_view(), name='list'),
    path('details/<int:pk>/', RestaurantDetails.as_view(), name='details')
]
