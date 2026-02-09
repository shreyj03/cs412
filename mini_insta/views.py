# File: mini_insta/views.py
# Author: Shrey Jain (shreyj@bu.edu), 2/9/26
# Description: Views for mini_insta application

from django.shortcuts import render
from django.views.generic import ListView
from .models import Profile
# Create your views here.

class ProfileListView(ListView):
    """View to display all profiles"""
    model = Profile
    template_name = 'mini_insta/show_all_profiles.html'
    context_object_name = 'profiles'