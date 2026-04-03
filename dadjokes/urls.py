# File: dadjokes/urls.py
# Author: Shrey Jain (shreyj@bu.edu), 4/3/2026
# Description: URL routing for dadjokes application

from django.urls import path
from . import views

urlpatterns = [
    path('', views.random_view, name='random'),
    path('random', views.random_view, name='random_alt'),
    path('jokes', views.jokes_view, name='jokes'),
    path('joke/<int:pk>', views.joke_detail_view, name='joke_detail'),
    path('pictures', views.pictures_view, name='pictures'),
    path('picture/<int:pk>', views.picture_detail_view, name='picture_detail'),

    # api endpoints
    path('api/', views.api_random_joke, name='api_random'),
    path('api/random', views.api_random_joke, name='api_random_alt'),
    path('api/jokes', views.api_jokes, name='api_jokes'),
    path('api/joke/<int:pk>', views.api_joke_detail, name='api_joke_detail'),
    path('api/pictures', views.api_pictures, name='api_pictures'),
    path('api/picture/<int:pk>', views.api_picture_detail, name='api_picture_detail'),
    path('api/random_picture', views.api_random_picture, name='api_random_picture'),
]