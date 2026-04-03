# File: dadjokes/serializers.py
# Author: Shrey Jain (shreyj@bu.edu), 4/3/2026
# Description: serializers for dadjokes REST API

from rest_framework import serializers
from .models import Joke, Picture

class JokeSerializer(serializers.ModelSerializer):
    '''serialize a Joke object to JSON'''
    class Meta:
        model = Joke
        fields = ['id', 'text', 'name', 'timestamp']

class PictureSerializer(serializers.ModelSerializer):
    '''serialize a Picture object to JSON'''
    class Meta:
        model = Picture
        fields = ['id', 'picture', 'name', 'timestamp']