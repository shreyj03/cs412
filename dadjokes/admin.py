from django.contrib import admin

# File: dadjokes/admin.py
# Author: Shrey Jain (shreyj@bu.edu), 4/3/2026
# Description: admin registration for dadjokes application

# Register your models here.
from .models import Joke, Picture
admin.site.register(Joke)
admin.site.register(Picture)