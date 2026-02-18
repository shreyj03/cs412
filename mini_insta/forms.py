# File: mini_insta/forms.py
# Author: Shrey Jain (shreyj@bu.edu), 2/17/2026
# Description: forms for mini_insta application

from django import forms
from .models import *

class CreatePostForm(forms.ModelForm):
    '''A form to add a post to the database.'''

    class Meta:
        '''associate this form with a model from our database.'''
        model = Post
        fields = ['caption']