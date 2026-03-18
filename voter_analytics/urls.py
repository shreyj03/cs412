# voter_analytics/urls.py
# Shrey Jain (shreyj@bu.edu)
# URL patterns for voter_analytics app

from django.urls import path
from . import views

urlpatterns = [
    path('', views.VotersListView.as_view(), name='voters'),
    path('voter/<int:pk>/', views.VoterDetailView.as_view(), name='voter'),
    path('graphs', views.GraphListView.as_view(), name='graphs'),
]