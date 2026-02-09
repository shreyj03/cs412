# File: mini_insta/urls.py
# Author: Shrey Jain (shreyj@bu.edu), 2/9/26
# Description: Urls for mini_insta application

from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProfileListView.as_view(), name='show_all_profiles'),
]