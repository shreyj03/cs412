# File: quotes/views.py
# Author: Shrey Jain (shreyj@bu.edu), 1/26/2026
# Description: Views for quotes application

from django.http import HttpResponse
from django.shortcuts import render
import random
import time

michael_scott_quotes = [
    "I'm not superstitious, but I am a little stitious.",
    "Would I rather be feared or loved? Easy. Both. I want people to be afraid of how much they love me.",
    "That's what she said."
]

michael_scott_pictures = [
    "https://miro.medium.com/1*-SoJy52kgGuN9Fj9jmIb0Q.png",
    "https://i.pinimg.com/736x/d9/ca/d3/d9cad34c676e94ceb9c7edf37c8efa24.jpg",
    "https://upload.wikimedia.org/wikipedia/en/5/56/PrisonMike.png"
]

def quote_page(request):
    '''Respond to the url 'quote.html', delegate work to a template.'''
    template_name = 'quotes/quote.html'
    context = {
        "quote": michael_scott_quotes[random.randint(0, len(michael_scott_quotes) - 1)],
        "image": michael_scott_pictures[random.randint(0, len(michael_scott_pictures) - 1)],
        "time": time.ctime()
    }
    return render(request, template_name, context)

def show_all_page(request):
    '''Respond to the url 'show_all.html', delegate work to a template.'''
    template_name = 'quotes/show_all.html'
    context = {
        "quotes": michael_scott_quotes,
        "images": michael_scott_pictures,
        "time": time.ctime()
    }
    return render(request, template_name, context)

def about_page(request):
    '''Respond to the url 'about_page.html', delegate work to a template.'''
    template_name = 'quotes/about.html'
    context = {
        "time": time.ctime()
    }
    return render(request, template_name, context)